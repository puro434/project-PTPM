import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

# 1. Получение списка пользователей (GET /users)
def test_get_users_list():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)
    assert len(users) > 0
    for user in users:
        assert "id" in user
        assert "name" in user
        assert "username" in user
        assert "email" in user

# 2. Получение конкретного пользователя (GET /users/{id})
def test_get_single_user():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == 1
    assert user["name"] == "Leanne Graham"
    assert user["email"] == "Sincere@april.biz"

# 3. Негативный тест: запрос несуществующего пользователя (404)
def test_get_nonexistent_user():
    response = requests.get(f"{BASE_URL}/users/9999")
    assert response.status_code == 404

# 4. Создание нового пользователя (POST /users)
def test_create_user():
    new_user = {
        "name": "Ivan Petrov",
        "username": "ivanp",
        "email": "ivan@example.com"
    }
    response = requests.post(f"{BASE_URL}/users", json=new_user)
    assert response.status_code == 201
    created_user = response.json()
    assert "id" in created_user
    assert created_user["name"] == "Ivan Petrov"

# 5. Обновление информации (PUT /users/{id})
def test_update_user():
    updated_data = {"name": "New Name", "email": "new@example.com"}
    response = requests.put(f"{BASE_URL}/users/1", json=updated_data)
    assert response.status_code == 200
    updated_user = response.json()
    assert updated_user["name"] == "New Name"
    assert updated_user["email"] == "new@example.com"

# 6. Удаление пользователя (DELETE /users/{id})
def test_delete_user():
    response = requests.delete(f"{BASE_URL}/users/1")
    assert response.status_code in (200, 204)

# 7. Дополнительно: Параметризованный тест
@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_multiple_users(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id