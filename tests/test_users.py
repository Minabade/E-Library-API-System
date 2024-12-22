from fastapi.testclient import TestClient
from unittest.mock import patch
from main import *
from uuid import UUID, uuid4

client = TestClient(app)

mock_users: dict[str, User] = {
    "8e29f6e1-093d-4adf-90c3-83031e88d502": User(
        id="8e29f6e1-093d-4adf-90c3-83031e88d502",
        name="Jane Doe",
        email="jane.doe@example.com",
        is_active=True
    ),
    "f8b07f85-2fa8-45c2-8dbb-d19d64a8a7b1": User(
        id="f8b07f85-2fa8-45c2-8dbb-d19d64a8a7b1",
        name="John Smith",
        email="john.smith@example.com",
        is_active=False
    )
}



@patch("routers.user.users", mock_users)
def test_get_all_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json()["data"] == [
    {
        "id": "8e29f6e1-093d-4adf-90c3-83031e88d502",
        "name": "Jane Doe",
        "email": "jane.doe@example.com",
        "is_active": True
    },
    {
        "id": "f8b07f85-2fa8-45c2-8dbb-d19d64a8a7b1",
        "name": "John Smith",
        "email": "john.smith@example.com",
        "is_active": False
    }
]
        

@patch("main.users", mock_users)
@patch("crud.user.uuid4", return_value="b17ea86e-55be-4b4e-b4f1-93ca4f2446bf")
def test_create_user(mock_uuid):
    user_data = {
        "name": "Giant Smith",
        "email": "giant.smith@example.com",
        "is_active": True
    }
    expected_user_response = {
        "id": "b17ea86e-55be-4b4e-b4f1-93ca4f2446bf",
        "name": "Giant Smith",
        "email": "giant.smith@example.com",
        "is_active": True
    }
    response = client.post("/users/signup", json=user_data)
    assert response.status_code == 201
    assert response.json()["data"] == expected_user_response




@patch("crud.user.users", mock_users)
def test_get_user_by_id():
    response = client.get("/users/8e29f6e1-093d-4adf-90c3-83031e88d502")
    assert response.status_code == 200
    assert response.json()["data"] ==  {
        "id": "8e29f6e1-093d-4adf-90c3-83031e88d502",
        "name": "Jane Doe",
        "email": "jane.doe@example.com",
        "is_active": True
    }

@patch("routers.user.users", mock_users)
def test_update_user():
    user_data = {
        "name": "Updated User name"
       
    }
    expected_user_response = user_data = {
        "id": "8e29f6e1-093d-4adf-90c3-83031e88d502",
        "name": "Updated User name",
        "email": "jane.doe@example.com",
        "is_active": True
    }
    
    response = client.put("/users/8e29f6e1-093d-4adf-90c3-83031e88d502", json=user_data)
    assert response.status_code == 200
    assert response.json()["data"] == expected_user_response

@patch("routers.user.users", mock_users)
def test_partially_update_user():
    user_data = {
        "name": "Updated User name"
       
    }
    expected_user_response = user_data = {
        "id": "8e29f6e1-093d-4adf-90c3-83031e88d502",
        "name": "Updated User name",
        "email": "jane.doe@example.com",
        "is_active": True
    }
    
    response = client.patch("/users/8e29f6e1-093d-4adf-90c3-83031e88d502", json=user_data)
    assert response.status_code == 200
    assert response.json()["data"] == expected_user_response    

@patch("routers.user.users", mock_users)
def test_deactivate_user():
    response = client.patch("/users/8e29f6e1-093d-4adf-90c3-83031e88d502/deactivate")
    assert response.status_code == 200
    assert response.json()["data"] == {
        "id": "8e29f6e1-093d-4adf-90c3-83031e88d502",
        "name": "Updated User name",
        "email": "jane.doe@example.com",
        "is_active": False
    }    

@patch("routers.user.users", mock_users)
def test_delete_user():
    response = client.delete("/users/8e29f6e1-093d-4adf-90c3-83031e88d502/delete")
    assert response.status_code == 204
    response = client.get("/users/f8e29f6e1-093d-4adf-90c3-83031e88d502")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


   

        
   
   