from fastapi import APIRouter

from common.response.schema import responseBase
from schemas.image import HttpResizeImage, HttpConvertImage
from services.image import ImageService

router = APIRouter()


@router.post("/resize", summary="调整图片尺寸")
async def resize(obj: HttpResizeImage):
    resp = await ImageService.resize(obj)
    return await responseBase.success(data=resp)


@router.post("/convert", summary="转换图片格式")
async def convert(obj: HttpConvertImage):
    resp = await ImageService.convert(obj)
    return await responseBase.success(data=resp)
