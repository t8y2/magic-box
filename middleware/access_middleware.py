import time
from datetime import datetime

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from logger.logger import log


class AccessMiddleware(BaseHTTPMiddleware):
    """
    记录请求日志
    """

    async def dispatch(self, request: Request, call_next) -> Response:
        request_id = int(time.time())

        start_time = datetime.now()
        log.info(f'Request {request.method} {request.url} {request.client.host}:{request.client.port} {request_id}')
        response = await call_next(request)
        end_time = datetime.now()
        log.info(f'Response {response.status_code} {request.url} {end_time - start_time} {request_id}')
        return response
