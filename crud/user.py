from fastapi import HTTPException, status
from schemas.user import User, UserCreate, UserUpdate, UserPatch, users
from uuid import uuid4




class UserCrud():

    @staticmethod
    def create_user(new_user: UserCreate):
        user_id = str(uuid4())
        user  = User(id = user_id, **new_user.model_dump())
        users[user_id]=user
        return user

    @staticmethod
    def get_user_by_id(user_id: str):
        user = users.get(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    
    @staticmethod
    def update_user(user_id: str, new_data:UserUpdate):
        user: User= user_crud.get_user_by_id(user_id)
        for k, v in new_data.model_dump().items():
            setattr(user, k, v)
        return user
    
    @staticmethod
    def partially_update_user(user_id: str, new_data:UserPatch):
        user: User= user_crud.get_user_by_id(user_id)
        for k, v in new_data.model_dump(exclude_unset=True).items():
            setattr(user, k, v)
        return user
    
    @staticmethod
    def deactivate_user(user_id: str):
        user: User= user_crud.get_user_by_id(user_id)
        user.is_active = False
        return user
    
    @staticmethod
    def  delete_user(user_id: str):
        user: User= user_crud.get_user_by_id(user_id)
        del users[user_id]
        return



     






user_crud = UserCrud()
