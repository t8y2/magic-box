from pydantic import Field

from schemas.base import BaseSchema


class HttpImageBase(BaseSchema):
    file_name: str = Field(..., description="文件名")
    file_uri: str = Field(..., description="图片地址")


class HttpImageResize(HttpImageBase):
    width: int | None = Field(None, description="图片宽度", gt=0)  # 宽度可以为 None
    height: int | None = Field(None, description="图片高度", gt=0)  # 高度可以为 None


class HttpImageConvert(HttpImageBase):
    final_type: str = Field(..., description="需要转换的类型")
