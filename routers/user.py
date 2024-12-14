from uuid import UUID
from fastapi import APIRouter, status, Path
from crud.user import user_crud
from schemas.user import users, User, UserCreate, UserUpdate, UserPatch
from typing import Annotated


user_router = APIRouter()

@user_router.get("/", status_code=status.HTTP_200_OK)
async def get_all_users():
    return {"data": list(users.values()), "message": "successful"}

@user_router.post("/signup", status_code=status.HTTP_201_CREATED)
async def  create_user(new_user: UserCreate):
    user = user_crud.create_user(new_user)
    return {"data": user, "message": "user created successfully"}

@user_router.get("/{user_id}",  status_code=status.HTTP_200_OK)
async def get_user_by_id(user_id: Annotated[str, Path()]):
    user =  user_crud.get_user_by_id(user_id)
    return {"data": user, "message": "successful"}

@user_router.put("/{user_id}",  status_code=status.HTTP_200_OK)
async def update_user(user_id: str, new_data:UserUpdate):
    user =  user_crud.update_user(user_id, new_data)
    return {"data": user, "message": "user updated successfully"}

@user_router.patch("/{user_id}",  status_code=status.HTTP_200_OK)
async def partially_update_user(user_id: str, new_data:UserPatch):
    user =  user_crud.partially_update_user(user_id, new_data)
    return {"data": user, "message": "user updated successfully"}

@user_router.patch("/{user_id}/deactivate",  status_code=status.HTTP_200_OK)
async def deactivate_user(user_id: str):
    user =  user_crud.deactivate_user(user_id)
    return {"data": user, "message": "user deactivated successfully"}

@user_router.delete("/{user_id}/delete",  status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: str):
    user =  user_crud.delete_user(user_id)
    return {"data": user, "message": "user deleted successfully"}

