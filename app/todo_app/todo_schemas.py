from enum import Enum

from pydantic import BaseModel


class CreateTodoSchema(BaseModel):
    name: str


class UpdateTodoSchema(BaseModel):
    id: int | None = None
    name: str | None = None


class SecureTodosModel(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
