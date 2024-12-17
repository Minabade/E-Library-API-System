from datetime import datetime
from fastapi import HTTPException, status
from schemas.borrow import Borrow_Record, BorrowRequest, borrow_records, Borrow_Record_Out
from schemas.book import books, Book
from schemas.user import users,User
from crud.user import user_crud
from crud.book import book_crud
from uuid import uuid4, UUID
from typing import Any



class BorrowCrud():
    @staticmethod
    def get_borrow_record(user_id: str):
        user: User= user_crud.get_user_by_id(user_id)
        user_borrow_records = []
        for record in borrow_records.values():
            record: Borrow_Record
            if record.user_id == user_id:
                user_borrow_records.append(record)
        if not user_borrow_records:
            raise HTTPException(status_code=404, detail="No borrow record for this user")
        return user_borrow_records
       
             

    @staticmethod
    def get_pending_returns(book_id:int):
        book = book_crud.get_book_by_id(book_id)
        for id,v in borrow_records.items():
            v: Borrow_Record
            if v.book_id == book_id and v.return_date == None:
                return v      
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book is not pending return")
           
               

    @staticmethod
    def borrow_book(user_id: str, borrow_book: BorrowRequest) :
        user: User= user_crud.get_user_by_id(user_id)
        if not user.is_active:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Book can not be borrowed by an inactive user")
        for id, book in books.items():
            book: Book
            if book.title == borrow_book.title and book.author == borrow_book.author:
                if not book.is_available:
                    raise HTTPException(status_code=404, detail="Book is not available")
                borrow_record_id = len(borrow_records) + 1
                borrow_record = Borrow_Record(id=borrow_record_id, book_id=book.id, user_id=user_id, borrow_date=datetime.now(), return_date=None)
                borrow_records[borrow_record_id]=borrow_record
                book.is_available = False
                return borrow_record
        raise HTTPException(status_code=404, detail="Book not found")
        
    
    
    # @staticmethod
    # def return_book(book_id: int):
    #     book: Book= book_crud.get_book_by_id(book_id)
        
    #     if book.is_available:
    #         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="book is already available")
    #     borrow_record: Borrow_Record = borrow_crud.get_pending_returns(book_id=book_id)
    #     borrow_record.return_date = datetime.now()
    #     borrow_records[borrow_record.id]=borrow_record
    #     data = borrow_record.model_dump(exclude=["id"])
    #     book.is_available =  True
    #     return data
            

    @staticmethod
    def return_book(borrow_id: int):
        borrows = borrow_records.get(borrow_id)
        if not borrows:
            raise HTTPException(status_code=404, detail="Borrow record not found")
        if borrows.return_date  != None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no pending return")
        

        borrows.return_date = datetime.now()
        borrow_records[borrow_id]=borrows
        data = borrows.model_dump(exclude=["id"])
        book_id = borrow_records.get(borrow_id).book_id
        book = book_crud.get_book_by_id(book_id)
        book.is_available=  True
        return data

            
              
            
borrow_crud = BorrowCrud()