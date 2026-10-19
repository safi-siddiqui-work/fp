from fastapi import APIRouter

from .todo_schemas import CreateTodoSchema, UpdateTodoSchema
from .todo_services import createTodosService, getTodosService, updateTodosService

router = APIRouter()


@router.get("/todos")
async def getTodosRoute():
    res = await getTodosService()
    return res


@router.post("/todos")
async def createTodosRoute(createTodoSchema: CreateTodoSchema):
    res = await createTodosService(createTodoSchema)
    return res


@router.patch("/todos/{todoId}")
async def udpateTodosRoute(todoId: int, updateTodoSchema: UpdateTodoSchema):
    res = await updateTodosService(
        updateTodoSchema=UpdateTodoSchema(id=todoId, name=updateTodoSchema.name)
    )
    return res
