from enum import Enum

from common.exception.handler import create_custom_exception


class ImageStatus(Enum):
    DOWNLOAD_ERROR = (3000, "下载失败")
    MISS_PARAMS = (3001, "缺少参数")

    @property
    def code(self):
        return self.value[0]

    @property
    def msg(self):
        return self.value[1]


# 创建异常类
DownloadError = create_custom_exception(ImageStatus.DOWNLOAD_ERROR)
MissingParams = create_custom_exception(ImageStatus.MISS_PARAMS)
