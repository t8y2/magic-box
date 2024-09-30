from fastapi import APIRouter
from core.config import settings
from controller.v1.user import router as user_router

v1 = APIRouter(prefix=settings.FASTAPI_API_PREFIX)
v1.include_router(user_router, prefix='/user', tags=["用户"])
