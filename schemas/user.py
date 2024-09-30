from datetime import datetime
from pydantic import Field

from schemas.base import BaseSchema


class HttpLogin(BaseSchema):
    username: str
    password: str


# 用户注册
class HttpCreateUser(BaseSchema):
    username: str = Field(..., min_length=3, max_length=50, description="用户名")
    alias: str | None = Field(None, max_length=100, description="用户别名，可选")
    password: str = Field(..., min_length=6, max_length=100, description="用户密码")
    is_active: bool = Field(..., description="用户是否激活")
    is_superuser: bool = Field(..., description="用户是否为超级管理员")
    roles: list[str] = Field(..., min_items=1, description="用户角色列表")
    note: str | None = Field(None, max_length=255, description="备注信息")


# 创建用户
class DataBaseCreateUser(BaseSchema):
    uid: str = Field(..., min_length=3, max_length=50, description="用户唯一标识")
    username: str = Field(..., min_length=3, max_length=50, description="用户名")
    alias: str | None = Field(None, max_length=100, description="用户别名，可选")
    password: str = Field(..., min_length=6, max_length=100, description="用户密码")
    is_active: bool = Field(..., description="用户是否激活")
    is_superuser: bool = Field(..., description="用户是否为超级管理员")
    roles: list[str] = Field(..., min_items=1, description="用户角色列表")
    note: str | None = Field(None, max_length=255, description="备注信息")
    created_at: datetime = Field(datetime.now(), description="用户创建时间")
    last_login: datetime = Field(..., description="用户上次登录时间")
