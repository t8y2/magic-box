import asyncio
from typing import List

from dao.base import BaseDao
from database.mongo import user_collection
from schemas.user import DataBaseCreateUser


class UserDao(BaseDao):
    @classmethod
    async def create_user(cls, obj: DataBaseCreateUser):
        await user_collection.insert_one(obj.model_dump())

    @classmethod
    async def get_by_uid(cls, uid: str):
        return await user_collection.find_one({"uid": uid})

    @classmethod
    async def get_by_username(cls, username: str):
        return await user_collection.find_one({"username": username})

    @classmethod
    async def list_user(cls):
        return await user_collection.find({}).to_list(length=None)  # 转换为列表

