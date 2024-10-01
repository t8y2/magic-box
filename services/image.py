import asyncio
from io import BytesIO
import requests
from PIL import Image
from common.response.code_image import DownloadError, MissingParams
from schemas.image import HttpImageResize, HttpImageConvert, HttpImageBase


class ImageService(object):
    @classmethod
    async def download(cls, url: str):
        response = requests.get(url)
        if response.status_code != 200:
            raise DownloadError()
        return BytesIO(response.content)

    @classmethod
    async def resize(cls, obj: HttpImageResize):
        img_data = await cls.download(obj.file_uri)
        with Image.open(img_data) as img:
            original_width, original_height = img.size
            # 如果没有提供宽度或高度，则按比例缩放
            if obj.width is None and obj.height is None:
                raise MissingParams("height or width")
            if obj.width is None:
                # 根据高度缩放
                aspect_ratio = original_width / original_height
                obj.width = int(obj.height * aspect_ratio)
            elif obj.height is None:
                # 根据宽度缩放
                aspect_ratio = original_height / original_width
                obj.height = int(obj.width * aspect_ratio)
            resized_img = img.resize((obj.width, obj.height))
            resized_img.show()
            # 上传对象存储逻辑待完善
            return {"file_url": "mock_url"}

    @classmethod
    async def convert(cls, obj: HttpImageConvert):
        img_data = await cls.download(obj.file_uri)
        with Image.open(img_data) as img:
            # 将图片保存到内存的二进制对象中，而不是保存到本地
            img_byte_array = io.BytesIO()
            img.save(img_byte_array, format=obj.final_type.upper())
            img_byte_array.seek(0)  # 重置文件指针到开始位置
            img.show()

    @classmethod
    async def rmbg(cls, obj: HttpImageBase):
        from transformers import pipeline
        pipe = pipeline("image-segmentation", model="briaai/RMBG-1.4", trust_remote_code=True)
        pillow_image = pipe(obj.file_uri)
        pillow_image.show()

    @classmethod
    async def HDRestore(cls):
        from diffusers import LDMSuperResolutionPipeline
        import torch
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model_id = "CompVis/ldm-super-resolution-4x-openimages"

        pipeline = LDMSuperResolutionPipeline.from_pretrained(model_id)
        pipeline = pipeline.to(device)

        url = "https://user-images.githubusercontent.com/38061659/199705896-b48e17b8-b231-47cd-a270-4ffa5a93fa3e.png"
        response = requests.get(url)
        low_res_img = Image.open(BytesIO(response.content)).convert("RGB")
        low_res_img = low_res_img.resize((128, 128))

        upscaled_image = pipeline(low_res_img, num_inference_steps=100, eta=1).images[0]
        upscaled_image.save("ldm_generated_image.png")


if __name__ == '__main__':
    asyncio.run(
        ImageService.HDRestore()
    )
