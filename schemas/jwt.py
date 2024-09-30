from fastapi.security import OAuth2PasswordBearer
from pydantic import Field
from datetime import datetime

from schemas.base import BaseSchema

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")


class UserInfo(BaseSchema):
    uid: str = Field(..., min_length=3, max_length=50, description="用户唯一标识")
    username: str = Field(..., min_length=3, max_length=50, description="用户名")
    alias: str | None = Field(None, max_length=100, description="用户别名，可选")
    is_superuser: bool = Field(..., description="用户是否为超级管理员")
    roles: list[str] = Field(..., min_items=1, description="用户角色列表")
