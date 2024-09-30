from pydantic import Field

from schemas.base import BaseSchema


class HttpResizeImage(BaseSchema):
    file_name: str = Field(..., description="文件名")
    file_url: str = Field(..., description="图片地址")
    width: int | None = Field(None, description="图片宽度", gt=0)  # 宽度可以为 None
    height: int | None = Field(None, description="图片高度", gt=0)  # 高度可以为 None
