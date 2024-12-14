from uuid import UUID
from fastapi import APIRouter, status, Path
from crud.book import book_crud
from schemas.book import books, Book, BookCreate, BookUpdate, BookPatch
from typing import Annotated


book_router = APIRouter()




Book_router = APIRouter()

@book_router.get("/", status_code=status.HTTP_200_OK)
async def get_all_books():
    return {"data": list(books.values()), "message": "successful"}

@book_router.post("/signup", status_code=status.HTTP_201_CREATED)
async def  create_book(new_book: BookCreate):
    book = book_crud.create_book(new_book)
    return {"data": book, "message": "book created successfully"}

@book_router.get("/{book_id}",  status_code=status.HTTP_200_OK)
async def get_book_by_id(book_id: Annotated[int, Path()]):
    book =  book_crud.get_book_by_id(book_id)
    return {"data": book, "message": "successful"}

@book_router.put("/{book_id}",  status_code=status.HTTP_200_OK)
async def update_book(book_id: int, new_book:BookUpdate):
    book =  book_crud.update_book(book_id, new_book)
    return {"data": book, "message": "book updated successfully"}

@book_router.patch("/{book_id}",  status_code=status.HTTP_200_OK)
async def partially_update_book(book_id: int, new_book:BookPatch):
    book =  book_crud.partially_update_book(book_id, new_book)
    return {"data": book, "message": "book updated successfully"}

@book_router.patch("/{book_id}/deactivate",  status_code=status.HTTP_200_OK)
async def deactivate_book(book_id: int):
    book =  book_crud.deactivate_book(book_id)
    return {"data": book, "message": "book is not available"}

@book_router.delete("/{book_id}/delete",  status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    book =  book_crud.delete_book(book_id)
    return {"data": book, "message": "book deleted successfully"}

