from fastapi import APIRouter
from config.db import create_db_and_tables
routes_create = APIRouter()

@routes_create.on_event("startup")
def on_startup():
    create_db_and_tables()


