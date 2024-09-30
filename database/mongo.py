import sys
from motor.motor_asyncio import AsyncIOMotorClient
from core.config import settings
from logger.logger import log

mongo_connection_string = f"mongodb://{settings.MONGO_USER}:{settings.MONGO_PASSWORD}@{settings.MONGO_HOST}:{settings.MONGO_PORT}/"

mongo_client = AsyncIOMotorClient(mongo_connection_string)

db = mongo_client[settings.MONGO_DB]  # 指定数据库名

user_collection = db["user"]  # 用户表


async def test_mongo():
    try:
        await db.list_collection_names()
        print(f"✅ 数据库 mongodb 连接认证成功!")
    except Exception as e:
        log.error('❌ 数据库 mongodb 连接认证失败')
        sys.exit()
