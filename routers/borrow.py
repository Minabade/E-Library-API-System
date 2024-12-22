from fastapi import APIRouter, status
from crud.borrow import borrow_crud
from schemas.borrow import Borrow_Record, BorrowRequest, borrow_records, Borrow_Record_Out
from schemas.book import books, Book
from schemas.user import users,User
from crud.user import user_crud
from typing import Dict





borrow_router = APIRouter()

@borrow_router.post("/{user_id}/borrow_book", status_code=status.HTTP_201_CREATED)
async def borrow_book(user_id: str, borrow_book: BorrowRequest):
    borrow_record =  borrow_crud.borrow_book(user_id, borrow_book)
    return {"data": borrow_record,  "message": "book borrowed successfully"}

@borrow_router.patch("/{borrow_id}/return_book", status_code=status.HTTP_200_OK)
async def return_book(borrow_id:int)->Dict:
    borrow_record =  borrow_crud.return_book(borrow_id)
    return {"data":borrow_record, "message": "book returned successfully"}

@borrow_router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_borrow_record(user_id: str):
    user_borrow_records =  borrow_crud.get_borrow_record(user_id)
    return {"user borrow record": user_borrow_records}

@borrow_router.get("/", status_code=status.HTTP_200_OK)
async def get_borrow_records():
    return borrow_records   

@borrow_router.get("/borrow_record/{book_id}", status_code=status.HTTP_200_OK)
async def get_pending_returns(book_id:int):
    borrow_record = borrow_crud.get_pending_returns(book_id)
    return {"pending returns": borrow_record}


