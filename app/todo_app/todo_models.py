from sqlmodel import Field, SQLModel


class TodoModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str | None = Field(default=None)
