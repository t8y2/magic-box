from fastapi import APIRouter

from common.response.schema import responseBase
from schemas.image import HttpResizeImage
from services.image import ImageService

router = APIRouter()


@router.post("/resize", summary="调整图片尺寸")
async def resize(obj: HttpResizeImage):
    resp = await ImageService.resize(obj)
    return await responseBase.success(data=resp)


# 示例调用
