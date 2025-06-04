from fastapi import APIRouter, Query, HTTPException
from config.db import session_dep
from schemas.User import UserPublic, UserCreate, User, UserUpdate
from typing import Annotated
from sqlmodel import select
routes_user = APIRouter()

@routes_user.get("/user/", response_model=list[UserPublic])
def get_users(
    session: session_dep, 
    offset: int = 0, 
    limit: Annotated[int, Query(len=100)] = 100
    ):
    users = session.exec(select(User).offset(offset).limit(limit)).all()
    return users

@routes_user.get("/user/{user_id}", response_model=UserPublic)
def get_user(user_id: int, session: session_dep):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@routes_user.post("/user/", response_model=UserPublic)
def create_users(user: UserCreate, session: session_dep):

    db_user = User.model_validate(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@routes_user.patch("/user/{user_id}", response_model=UserPublic)
def update_user(user_id: int, user: UserUpdate, session: session_dep):
        user_db = session.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        user_data = user.model_dump(exclude_unset=True)
        user_db.sqlmodel_update(user_data)
        session.add(user_db)
        session.commit()
        session.refresh(user_db)
        return user_db

@routes_user.delete("/user/{user_id}")
def update_user(user_id: int, session: session_dep):
        user_db = session.get(User, user_id)
        if not user_db:
            raise HTTPException(status_code=404, detail="User not found")
        session.delete(user_db)
        session.commit()
        return {"ok" : True}
