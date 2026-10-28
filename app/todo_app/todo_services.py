from .todo_schemas import CreateTodoSchema, SecureTodosModel, UpdateTodoSchema


async def getTodosService(skip: int = 0):
    return {"msg": "Todos List"}


async def getSecureTodosService(secure: SecureTodosModel):
    if secure is secure.alexnet:
        return {"msg": "Alex", "name": secure}

    if secure is secure.lenet:
        return {"msg": "Len", "name": secure}

    return {"msg": "Res", "name": secure}


async def createTodosService(createTodoSchema: CreateTodoSchema):
    print(createTodoSchema)
    return {"todo": createTodoSchema}


async def updateTodosService(id: int, updateTodoSchema: UpdateTodoSchema):
    print(id, updateTodoSchema)
    return {"msg": "Update TODO"}
