import sys

from redis.client import Redis
from redis.exceptions import AuthenticationError, TimeoutError

from logger.logger import log
from core.config import settings

# 创建redis连接对象
redis_client = Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    password=settings.REDIS_PASSWORD,
    db=settings.REDIS_DB,
)


async def test_redis():
    try:
        redis_client.ping()
        print(f"✅ 数据库 redis 连接认证成功!")
    except TimeoutError:
        log.INFO('❌ 数据库 redis 连接超时')
        sys.exit()
    except AuthenticationError:
        log.INFO('❌ 数据库 redis 连接认证失败')
        sys.exit()
    except Exception as e:
        log.INFO('❌ 数据库 redis 连接异常 {}', e)
        sys.exit()
