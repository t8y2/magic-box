from common.response.code_base import BaseStatus
from common.response import StatusEnum


class BaseCustomException(Exception):
    """
    自定义异常 基类
    """

    def __init__(self, msg: str, status: StatusEnum, data=None):
        self.status = status
        self.msg = msg
        self.data = data
