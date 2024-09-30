import asyncio
from typing import List

from dao.base import BaseDao
from database.mongo import user_collection, role_collection, route_collection
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

    @classmethod
    async def get_menus(cls, roles: List[str]) -> List[dict]:
        # 1. 如果是超级管理员角色，直接返回所有路由
        if "superuser" in roles:
            return await route_collection.find(
                {"meta.requireAuth": {"$ne": False}},  # 过滤掉 requireAuth 为 false 的路由
                {'_id': 0, 'alias': 0}
            ).to_list(length=None)

        # 2. 查找所有角色对应的菜单路径，去重
        menu_set = set()
        for role in roles:
            res = await role_collection.find_one({"name": role})
            if res:
                menu_paths = res.get("menus", [])
                menu_set.update(menu_paths)

        # 3. 在 route_collection 中查找所有以 menu 开头的路由，并过滤掉 requireAuth 为 false 的路由
        matched_routes = await route_collection.find(
            {
                "path": {"$regex": f"^({'|'.join(menu_set)})"},
                "meta.requireAuth": {"$ne": False}  # 过滤掉 requireAuth 为 false 的路由
            },
            {'_id': 0, 'alias': 0}
        ).to_list(length=None)
        return matched_routes


if __name__ == "__main__":
    asyncio.run(UserDao.get_menus(["uploader", "superuser"]))
