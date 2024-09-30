# 用户认证接口
from typing import List

from fastapi import APIRouter, Depends
from common.response.schema import responseBase
from schemas.jwt import UserInfo
from schemas.user import *
from services.jwt import JwtService
from services.user import UserService

router = APIRouter()


@router.get("/info", summary="获取用户信息")
async def user_info(user: UserInfo = Depends(JwtService.get_current_user)):
    return await responseBase.success(data=user)


@router.post("/login", summary="账号密码登录")
async def login(obj: HttpLogin):
    resp = await UserService.login(obj)
    return await responseBase.success(data=resp)


@router.post("/create", summary="新建用户")
async def create_user(obj: HttpCreateUser):
    await UserService.create_user(obj)
    return await responseBase.success()


@router.get("/list", summary="获取用户列表")
async def list_user():
    await UserService.list_user()
    return await responseBase.success()


@router.get("/menu", summary="获取用户路由")
async def get_menu(user: UserInfo = Depends(JwtService.get_current_user)):
    resp = await UserService.get_menus(user.roles)
    return await responseBase.success(data=resp)
