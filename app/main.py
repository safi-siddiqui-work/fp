from fastapi import FastAPI

from .todo_app import todo_routes

app = FastAPI()

app.include_router(todo_routes.router)
