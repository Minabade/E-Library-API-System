from fastapi.testclient import TestClient
from unittest.mock import patch
from main import *
from uuid import UUID, uuid4
from datetime import datetime

client = TestClient(app)

mock_borrows: dict[int, Borrow_Record] = {
    1: Borrow_Record(
        id=1,
        user_id="8e29f6e1-093d-4adf-90c3-83031e88d502",
        book_id=1,
        borrow_date=datetime(2024, 12, 19, 12, 0, 0),
        return_date=None
    ),
    2: Borrow_Record(
        id=2,
        user_id="b5341c10-2d99-4d4c-a34f-39d80f98a7a2",
        book_id=2,
        borrow_date=datetime(2024, 12, 19, 12, 0, 0),
        return_date=None
    ),
  
}

@patch("routers.borrow.borrow_records", mock_borrows)
@patch("crud.borrow.datetime")
def test_get_borrow_records(mock_now):
    mock_now.now.return_value = datetime(2024, 12, 19, 12, 0, 0)
    mock_now.side_effect = lambda *args, **kwargs: datetime(*args, **kwargs) 
    
    response = client.get("/borrow_records")
    expected_mock_records = {str(k):{**v.model_dump(),
                                    "borrow_date": v.borrow_date.isoformat() if v.borrow_date else None,
                                    "return_date": v.return_date.isoformat() if v.return_date else None,} for k, v in mock_borrows.items()}
    assert response.status_code == 200
    assert response.json()== expected_mock_records



     
    
@patch("crud.borrow.borrow_records", mock_borrows)
@patch("crud.borrow.datetime")
def test_borrow_book(mock_now):
    mock_now.now.return_value = datetime(2024, 12, 19, 12, 0, 0)
    mock_now.side_effect = lambda *args, **kwargs: datetime(*args, **kwargs)
    borrow_data ={
    "title": "Pride and Prejudice",
    "author": "Jane Austen"
}
    mocked_borrow_date = mock_now.now().isoformat()
    expected_borrow_response = {
        "id":len(mock_borrows)+1,
        "user_id":"8e29f6e1-093d-4adf-90c3-83031e88d502",
        "book_id":4,
        "borrow_date":mocked_borrow_date,
        "return_date":None

    }
    response = client.post("/borrow_records/8e29f6e1-093d-4adf-90c3-83031e88d502/borrow_book", json=borrow_data)
    assert response.status_code == 201
    assert response.json()["data"] == expected_borrow_response

@patch("routers.borrow.borrow_records", mock_borrows)
@patch("crud.borrow.datetime")
def test_return_book(mock_now): 
    mock_now.now.return_value = datetime(2024, 12, 19, 12, 0, 0)
    mock_now.side_effect = lambda *args, **kwargs: datetime(*args, **kwargs)

    response = client.patch("/borrow_records/2/return_book")
    mocked_borrow_date = "2024-11-20T14:15:00"
    mocked_return_date = mock_now.now().isoformat()
    assert response.status_code == 200
    assert response.json()["data"] == {
    "user_id": "8e29f6e1-093d-4adf-90c3-83031e88d502",
    "book_id": 2,
    "borrow_date": mocked_borrow_date,
    "return_date": mocked_return_date
  }

@patch("routers.borrow.borrow_records", mock_borrows)
@patch("crud.borrow.datetime")
def test_get_borrow_record(mock_now):
    mock_now.now.return_value = datetime(2024, 12, 19, 12, 0, 0)
    mock_now.side_effect = lambda *args, **kwargs: datetime(*args, **kwargs)
    
    mocked_borrow_date_1 = mock_now.now().isoformat()
    mocked_borrow_date_2 = "2024-11-20T14:15:00"
    mocked_return_date = mock_now.now().isoformat()


    expected_borrow_response = [
        {
        "id":1,
        "user_id":"8e29f6e1-093d-4adf-90c3-83031e88d502",
        "book_id":1,
        "borrow_date":mocked_borrow_date_1,
        "return_date":None

        },
        {
        "id":2,
        "user_id":"8e29f6e1-093d-4adf-90c3-83031e88d502",
        "book_id":2,
        "borrow_date":mocked_borrow_date_2,
        "return_date":mocked_return_date
        }    
    ]  
    
    response = client.get("/borrow_records/8e29f6e1-093d-4adf-90c3-83031e88d502")

    assert response.status_code == 200
    assert response.json()["user borrow record"] == expected_borrow_response


     
    



   

        
