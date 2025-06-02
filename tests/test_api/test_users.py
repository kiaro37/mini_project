from http.client import responses

import requests

def test_get_single_user():
    response = requests.get("https://reqres.in/api/users/2")

    # Проверка, что ответ пришел с кодом 200
    assert response.status_code == 200

    # Получим JSON-данные из ответа
    data = response.json()

    # Проверим, что в ответе есть ключ 'data'
    assert "data" in data

    # Проверим конкретное значение
    assert data["data"]["first_name"] == "Janet"