from fastapi import FastAPI

from .core.db import create_db_and_tables
from .todo_app import todo_routes

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(todo_routes.router)
