from fastapi import APIRouter, status, Path
from crud.user import user_crud
from schemas.user import users, User, UserCreate
from typing import Annotated



user_router = APIRouter()

@user_router.get("/", status_code=status.HTTP_200_OK)
async def get_all_users():
    return {"data": list(users.values()), "message": "successful"}

@user_router.post("/signup", status_code=status.HTTP_201_CREATED)
async def  create_user(new_user: UserCreate):
    user = user_crud.create_user(new_user)
    return {"data": user, "message": "user created successfully"}

