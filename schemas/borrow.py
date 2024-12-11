from pydantic import BaseModel
from datetime import datetime

class Borrow_RecordBase(BaseModel):
    user_id: int
    book_id: int
    borrow_date: datetime = datetime.now()
    return_date: datetime = datetime.today()

class Borrow_Record(Borrow_RecordBase):
    id: int

borrow_records: dict[int:Borrow_Record] = {}
