from fastapi import HTTPException, status
from schemas.book import Book, BookCreate, BookUpdate, BookPatch, books
from uuid import uuid4,UUID




class BookCrud():

    @staticmethod
    def create_book(new_book: BookCreate):
        book_id = len(books) + 1
        book  = Book(id = book_id, **new_book.model_dump())
        books[book_id]=book
        return book

    @staticmethod
    def get_book_by_id(book_id: int):
        book = books.get(book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        return book
    
    @staticmethod
    def update_book(book_id: int, new_book:BookUpdate):
        book: Book= book_crud.get_book_by_id(book_id)
        for k, v in new_book.model_dump().items():
            setattr(book, k, v)
        return book
    
    @staticmethod
    def partially_update_book(book_id: int, new_book:BookPatch):
        book: Book= book_crud.get_book_by_id(book_id)
        for k, v in new_book.model_dump(exclude_unset=True).items():
            setattr(book, k, v)
        return book
    
    @staticmethod
    def deactivate_book(book_id: int):
        book: Book= book_crud.get_book_by_id(book_id)
        book.is_available = False
        return book
    
    @staticmethod
    def  delete_book(book_id: int):
        if  book_id not in books:
            raise HTTPException(status_code=404, detail="Book not found")
        del books[book_id]
        return

    
                 
                     
                 


      

                
               











book_crud = BookCrud()