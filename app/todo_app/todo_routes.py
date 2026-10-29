from typing import Annotated

from fastapi import APIRouter, Path, Query
from pydantic import AfterValidator

from .todo_schemas import (
    CreateTodoSchema,
    QueryParamsModel,
    SecureTodosModel,
    UpdateTodoSchema,
)
from .todo_services import (
    createTodosService,
    getSecureTodosService,
    getTodosService,
    updateTodosService,
)
from .todo_validations import utfValidation

router = APIRouter()


@router.get("/todos")
async def getTodosRoute(
    skip: int = 0,
    limit: int = 0,
    Q: int | None = None,
    q1: Annotated[str | None, Query(max_length=10)] = None,
):
    # skip, limit default - Q optional
    res = await getTodosService(skip=skip + limit)
    return res


@router.get("/todos/secure/{secure}")
async def getSecureTodosRoute(secure: SecureTodosModel):
    res = await getSecureTodosService(secure)
    return res


@router.post("/todos")
async def createTodosRoute(createTodoSchema: CreateTodoSchema):
    res = await createTodosService(createTodoSchema)
    return res


@router.patch("/todos/{todoId}")
async def udpateTodosRoute(todoId: int, updateTodoSchema: UpdateTodoSchema):
    res = await updateTodosService(todoId, updateTodoSchema)
    return res


@router.get("/todo_files/{filePath:path}")
async def mangeTodoFilePathRoute(filePath):

    return {"filePath": f"fileUrl/{filePath}"}


@router.get("/todos_multiple_queries")
async def getTodosMultipleQUeriesRoute(
    q: Annotated[list[str] | None, Query()] = None,
):
    res = {"items": q}
    return res


@router.get("/todos_alias_query")
async def getTodosAliasQueryRoute(
    q: Annotated[str | None, Query(alias="q-q")] = None,
):
    res = {"items": q}
    return res


@router.get("/todos_custom_validation")
async def getTodosCustomValidationRoute(
    q: Annotated[str | None, AfterValidator(utfValidation)] = None,
):
    res = {"q": q}
    return res


@router.get("/todo_path/{slug}/{id}")
async def getTodosPathRoute(
    slug: Annotated[
        str | None,
        Path(
            title="Todo path slug",
        ),
    ],
    id: Annotated[int | None, Path(title="Todo path id", gt=0)],
):
    res = {"id": id, "slug": slug}
    return res


@router.get("/todo_pydantic_query_params/")
async def getTPQRRoute(q: Annotated[QueryParamsModel, Query()]):
    res = {"q": q}
    return res
