from pydantic import BaseModel, EmailStr
from uuid import UUID



class UserBase(BaseModel):
    name: str
    email: EmailStr
    is_active: bool = True

class User(UserBase):
    id: UUID

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

users: dict[int:User] = {}