from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
from core.config import settings

# 使用连接不指定数据库的 URL
DATABASE_URL_WITHOUT_DB = f"mysql+asyncmy://{settings.MYSQL_USER}:{settings.MYSQL_PASSWORD}@{settings.MYSQL_HOST}:{settings.MYSQL_PORT}/?charset=utf8mb4"
async_engine_without_db = create_async_engine(DATABASE_URL_WITHOUT_DB, echo=False, future=True,
                                              pool_pre_ping=True)

# 指定数据库的URL
DATABASE_URL_WITH_DB = f"mysql+asyncmy://{settings.MYSQL_USER}:{settings.MYSQL_PASSWORD}@{settings.MYSQL_HOST}:{settings.MYSQL_PORT}/{settings.MYSQL_DB}?charset=utf8mb4"
async_engine = create_async_engine(DATABASE_URL_WITH_DB, echo=False, future=True, pool_pre_ping=True)


async def create_database_if_not_exists():
    async with async_engine_without_db.begin() as conn:
        # 检查数据库是否存在
        db_check_query = f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{settings.MYSQL_DB}'"
        result = await conn.execute(text(db_check_query))
        database_exists = result.scalar() is not None

        # 如果数据库不存在，则创建
        if not database_exists:
            create_db_query = f"CREATE DATABASE `{settings.MYSQL_DB}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
            await conn.execute(text(create_db_query))
            print(f"数据库 '{settings.MYSQL_DB}' 创建成功。")


async def test_mysql():
    # 确保数据库存在
    await create_database_if_not_exists()
    # 现在可以继续执行其他数据库操作
    sql = "SELECT COUNT(*) AS count FROM information_schema.TABLES"
    async with async_engine.begin() as con:
        result = await con.execute(text(sql))
        _ = result.scalar()
        print(f"✅ 数据库 Mysql 连接认证成功!")


