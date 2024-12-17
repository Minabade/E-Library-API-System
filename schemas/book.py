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


books: dict[int, Book] = {
    1: Book(id=1, title="The Catcher in the Rye", author="J.D. Salinger", is_available=False),
    2: Book(id=2, title="To Kill a Mockingbird", author="Harper Lee", is_available=False),
    3: Book(id=3, title="1984", author="George Orwell", is_available=False),
    4: Book(id=4, title="Pride and Prejudice", author="Jane Austen", is_available=True),
    5: Book(id=5, title="The Great Gatsby", author="F. Scott Fitzgerald", is_available=True),
}
