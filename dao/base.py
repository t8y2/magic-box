from typing import Any, Dict, Generic, Type, TypeVar

from pydantic import BaseModel
from sqlmodel import SQLModel, select
from sqlmodel.ext.asyncio.session import AsyncSession


# 原生mysql转列表
def to_list(results):
    column_names = list(results.keys())
    res = []
    for item in results:
        res.append({column_names[i]: item[i] for i in range(len(column_names))})
    return res


class BaseDao(object):
    pass
