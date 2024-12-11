from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str
    is_available: bool = True

class Book(BookBase):
    id: int

class BookCeate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

books: dict[int:Book] = {}
