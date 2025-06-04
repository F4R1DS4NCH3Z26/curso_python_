from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    fullname: str = Field(index=True)
    username: str = Field(index=True)

class User(UserBase, table=True):
    user_id: int = Field(default= None, primary_key=True)
    password: str 
    

class UserPublic(UserBase):
    user_id: int

class UserCreate(UserBase):
    password: str 

class UserUpdate(UserBase):
    fullname: str | None = None
    username: str | None = None
    password: str | None = None   
     
