import io
from io import BytesIO

import requests
from PIL import Image

from common.response.code_image import DownloadError, MissingParams
from schemas.image import HttpResizeImage, HttpConvertImage


class ImageService(object):
    @classmethod
    async def download(cls, url: str):
        response = requests.get(url)
        if response.status_code != 200:
            raise DownloadError()
        return BytesIO(response.content)

    @classmethod
    async def resize(cls, obj: HttpResizeImage):
        img_data = await cls.download(obj.file_url)
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
    async def convert(cls, obj: HttpConvertImage):
        img_data = await cls.download(obj.file_url)
        with Image.open(img_data) as img:
            # 将图片保存到内存的二进制对象中，而不是保存到本地
            img_byte_array = io.BytesIO()
            img.save(img_byte_array, format=obj.final_type.upper())
            img_byte_array.seek(0)  # 重置文件指针到开始位置
            img.show()
