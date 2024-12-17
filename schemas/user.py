from pydantic import BaseModel, EmailStr
from uuid import UUID, uuid4
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

class UserUpdate(BaseModel):
    name: str  = "Ammar"


class UserPatch(BaseModel):
    name: Optional[str] = "Sumayyah"  
  



users: dict[str, User] = {
    "8e29f6e1-093d-4adf-90c3-83031e88d502": User(
        id="8e29f6e1-093d-4adf-90c3-83031e88d502",
        name="Jane Doe",
        email="jane.doe@example.com",
        is_active=True
    ),
    "f8b07f85-2fa8-45c2-8dbb-d19d64a8a7b1": User(
        id="f8b07f85-2fa8-45c2-8dbb-d19d64a8a7b1",
        name="John Smith",
        email="john.smith@example.com",
        is_active=False
    ),
    "b5341c10-2d99-4d4c-a34f-39d80f98a7a2": User(
        id="b5341c10-2d99-4d4c-a34f-39d80f98a7a2",
        name="Alice Johnson",
        email="alice.johnson@example.com",
        is_active=True
    )
}
