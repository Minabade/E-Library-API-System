from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict

class Borrow_RecordBase(BaseModel):
    user_id: str
    book_id: int
    borrow_date: datetime = datetime.now()
    return_date: datetime|None = None

class Borrow_Record_Out(Borrow_RecordBase):
    pass

class Borrow_Record(Borrow_RecordBase):
    id: int

class BorrowRequest(BaseModel):
    title: str = "Pride and Prejudice"
    author: str = "Jane Austen"


borrow_records: Dict[int, Borrow_Record] = {
    1: Borrow_Record(
        id=1,
        user_id="8e29f6e1-093d-4adf-90c3-83031e88d502",
        book_id=1,
        borrow_date=datetime(2024, 12, 19, 12, 0, 0),
        return_date=None
    ),
    2: Borrow_Record(
        id=2,
        user_id="8e29f6e1-093d-4adf-90c3-83031e88d502",
        book_id=2,
        borrow_date=datetime(2024, 11, 20, 14, 15),
        return_date=None
    ),
    3: Borrow_Record(
        id=3,
        user_id="b5341c10-2d99-4d4c-a34f-39d80f98a7a2",
        book_id=3,
        borrow_date=datetime(2024, 12, 10, 9, 0),
        return_date=None
    ),
}