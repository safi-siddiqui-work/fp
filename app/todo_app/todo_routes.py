from fastapi import APIRouter

from .todo_schemas import CreateTodoSchema, SecureTodosModel, UpdateTodoSchema
from .todo_services import (
    createTodosService,
    getSecureTodosService,
    getTodosService,
    updateTodosService,
)

router = APIRouter()


@router.get("/todos")
async def getTodosRoute(skip: int = 0, limit: int = 0, Q: int | None = None):
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
