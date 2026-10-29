from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field


class CreateTodoSchema(BaseModel):
    name: str


class UpdateTodoSchema(BaseModel):
    name: str | None = None


class SecureTodosModel(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


class QueryParamsModel(BaseModel):
    p1: int = Field(0, gt=0, lt=101)
    p2: Literal["joy", "play"] = Field("joy")
    p3: bool = Field(True)


class TodoBodyModel(BaseModel):
    name: str
