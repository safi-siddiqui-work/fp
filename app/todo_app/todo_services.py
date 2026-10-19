from .todo_schemas import CreateTodoSchema, UpdateTodoSchema


async def getTodosService():
    return {"msg": "Todos List"}


async def createTodosService(createTodoSchema: CreateTodoSchema):
    print(createTodoSchema)
    return {"msg": "Create Todo"}


async def updateTodosService(updateTodoSchema: UpdateTodoSchema):
    print(updateTodoSchema)
    return {"msg": "Update TODO"}
