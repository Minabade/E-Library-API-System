from fastapi import FastAPI
from routers.user import user_router
from routers.book import book_router
from routers.borrow import borrow_router
from schemas.user import User, users
from schemas.book import Book,  books
from schemas.borrow import Borrow_Record, borrow_records

app = FastAPI()
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(book_router, prefix="/books", tags=["Books"])
app.include_router(borrow_router, prefix="/borrow_records", tags=["BorrowRecords"])