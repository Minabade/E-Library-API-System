from pydantic import BaseModel, EmailStr
from uuid import UUID
from typing import Optional



class UserBase(BaseModel):
    name: str  
    email: EmailStr
    is_active: bool = True

class User(UserBase):
    id: UUID

class UserCreate(UserBase):
    name: str  = "Sumayyah"
    email: EmailStr = "sumayyah@yahoo.com"
    is_active: bool = True

class UserUpdate(UserBase):
    name: str  = "Ammar"
    email: EmailStr = "ammar@yahoo.com"
    is_active: bool = True

class UserPatch(UserBase):
    name: Optional[str] = "Sumayyah"  
    email: Optional[EmailStr] =  "sumayyah@yahoo.com"
    is_active: Optional[bool] = True



users: dict[str:User] = {}