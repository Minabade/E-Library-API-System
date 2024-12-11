from fastapi import HTTPException
from schemas.user import UserBase, User, UserCreate, UserUpdate, users
from uuid import uuid4




class UserCrud():

    @staticmethod
    def create_user(new_user: UserCreate):
        user_id = uuid4()
        user  = User(id = user_id, **new_user.model_dump())
        users[user_id]=user
        return user






user_crud = UserCrud()
