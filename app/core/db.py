from sqlmodel import Field, Session, SQLModel, create_engine, select

from .utils import get_settings

engine = create_engine(get_settings().database_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
