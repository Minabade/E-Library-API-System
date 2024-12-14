from pydantic import BaseModel
from typing import Optional


class BookBase(BaseModel):
    title: str
    author: str
    is_available: bool = True

class Book(BookBase):
    id: int

class BookCreate(BookBase):
    title: str = "Simbi goes to school"
    author: str = "Rotimi Akanni"
    is_available: bool = True

class BookUpdate(BookBase):
    title: str = "Edet lives in Calabar"
    author: str = "Mina Bade"
    is_available: bool = True

class BookPatch(BookBase):
    title: Optional[str] = "Simbi goes to school"
    author: Optional[str] = "Rotimi Akanni"
    is_available: bool = True


books: dict[int:Book] = {}
