from sqlmodel import create_engine, MetaData, Field, Session, select, SQLModel
from fastapi import Depends
from typing import Annotated
engine = create_engine("mysql+pymysql://root:@localhost:3306/fastapi")

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
session_dep = Annotated[Session, Depends(get_session)]