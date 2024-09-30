from fastapi import APIRouter
from core.config import settings
from controller.v1.user import router as user_router
from controller.v1.image import router as image_router

v1 = APIRouter(prefix=settings.FASTAPI_API_PREFIX)
v1.include_router(user_router, prefix='/user', tags=["用户"])
v1.include_router(image_router, prefix='/image', tags=["图片"])
