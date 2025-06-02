import requests

BASE_URL = "http://127.0.0.1:5000/api/users"

def test_get_all_users():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_single_user():
    response = requests.get(f"{BASE_URL}/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Alice"

def test_create_user():
    payload = {"name": "David"}
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "David"

def test_update_user():
    payload = {"name": "Alice Updated"}
    response = requests.put(f"{BASE_URL}/1", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Alice Updated"

def test_delete_user():
    response = requests.delete(f"{BASE_URL}/2")
    assert response.status_code == 200
    assert response.json()["message"] == "User deleted"
