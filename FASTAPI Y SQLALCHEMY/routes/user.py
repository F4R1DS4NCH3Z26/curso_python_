from fastapi import APIRouter
from config.db import conn
from models.user import users
from schemas.user import User 
from cryptography.fernet import Fernet
key = Fernet.generate_key()
encrypted = Fernet(key)
user = APIRouter()

@user.get('/users')
def get_users():    
    return conn.execute(users.select()).fetchall()

@user.post('/users')
def create_users(user: User):
    new_user = {"name": user.name, "email": user.email}
    new_user['password'] = encrypted.encrypt(user.password.encode())
    print(new_user)
    return "hello world 2" 