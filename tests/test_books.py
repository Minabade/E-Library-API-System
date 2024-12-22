from fastapi.testclient import TestClient
from unittest.mock import patch
from main import *
from uuid import UUID, uuid4

client = TestClient(app)

mock_books: dict[int, Book] = {
    1: Book(id=1, title="Moby Dick", author="Herman Melville", is_available=True),
    2: Book(id=2, title="War and Peace", author="Leo Tolstoy", is_available=True),
    3: Book(id=3, title="War and Love", author="Len Tolstoy", is_available=False),
    4: Book(id=4, title="The Hobbit", author="J.R.R. Tolkien", is_available=True),
    5: Book(id=5, title="Anna Karenina", author="Leo Tolstoy", is_available=True)
    
}



@patch("routers.book.books", mock_books)
def test_get_all_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert response.json()["data"] == [
    {
        "id": 1,
        "title": "Moby Dick",
        "author": "Herman Melville",
        "is_available": True
    },
    {
        "id": 2,
        "title": "War and Peace",
        "author": "Leo Tolstoy",
        "is_available": True
    },
    {
        "id": 3,
        "title": "War and Love",
        "author": "Len Tolstoy",
        "is_available": False
    },
    {
        "id": 4,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "is_available": True
    },
    {
        "id": 5,
        "title": "Anna Karenina",
        "author": "Leo Tolstoy",
        "is_available": True
    }
    

]
        

@patch("routers.book.books", mock_books)
def test_create_book():
    book_data = {
        "title": "Ali and  Simbi",
        "author": "Samantha Green",
        "is_available": True
    }
    expected_book_response = book_data = {
        "id": len(mock_books) + 1,
        "title": "Ali and  Simbi",
        "author": "Samantha Green",
        "is_available": True
    }
    response = client.post("/books/signup", json=book_data)
    assert response.status_code == 201
    assert response.json()["data"] == expected_book_response




@patch("crud.book.books", mock_books)
def test_get_book_by_id():
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json()["data"] ==  {
        "id": 1,
        "title": "Moby Dick",
        "author": "Herman Melville",
        "is_available": True
    }

@patch("routers.book.books", mock_books)
def test_update_book():
    book_data = {
        "title": "Updated Book title"
       
    }
    expected_book_response = book_data = {
        "id": 1,
        "title": "Updated Book title",
        "author": "Moby Dick",
        "is_available": True
    }
    
    response = client.put("/books/1", json=book_data)
    assert response.status_code == 200
    assert response.json()["data"] == expected_book_response

@patch("routers.book.books", mock_books)
def test_partially_update_book():
    book_data = {
        "title": "Updated Book title"
       
    }
    expected_book_response = book_data = {
        "id": 1,
        "title": "Updated Book title",
        "author": "Moby Dick",
        "is_available": True
    }
    
    response = client.patch("/books/1", json=book_data)
    assert response.status_code == 200
    assert response.json()["data"] == expected_book_response    

@patch("routers.book.books", mock_books)
def test_deactivate_book():
    response = client.patch("/books/1/deactivate")
    assert response.status_code == 200
    assert response.json()["data"] == {
        "id": 1,
        "title": "Updated Book title",
        "author": "Moby Dick",
        "is_available": False
    }    

@patch("routers.book.books", mock_books)
def test_delete_book():
    response = client.delete("/books/1/delete")
    assert response.status_code == 204
    response = client.get("/books/1")
    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found"


   