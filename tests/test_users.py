import pytest
from faker import Faker
from user_module import UserStore

fake = Faker("ru_RU") # Русские имена и данные

# ФИКСТУРА: Создает чистое хранилище перед каждым тестом и очищает после
@pytest.fixture
def store():
    s = UserStore()
    yield s
    s.users.clear()

# ФИКСТУРА: Генерирует тестового пользователя
@pytest.fixture
def sample_user():
    return {
        "name": fake.first_name(),
        "age": fake.random_int(min=18, max=80),
        "email": fake.email()
    }

# 1. Позитивный тест: добавление и поиск
def test_add_and_find_user(store, sample_user):
    uid = store.add_user(sample_user["name"], sample_user["age"], sample_user["email"])
    found = store.get_user(uid)
    assert found is not None
    assert found["email"] == sample_user["email"]

# 2. Позитивный тест: получение списка
def test_get_all_users(store):
    for _ in range(3):
        store.add_user(fake.first_name(), fake.random_int(18, 80), fake.email())
    assert len(store.get_all_users()) == 3

# 3. Позитивный тест: удаление
def test_delete_user(store, sample_user):
    uid = store.add_user(sample_user["name"], sample_user["age"], sample_user["email"])
    store.delete_user(uid)
    assert store.get_user(uid) is None

# 4. Негативный тест (с использованием параметризации)
@pytest.mark.parametrize("name, age, email", [
    ("", 25, "test@mail.com"),             # Пустое имя
    ("I", 25, "test@mail.com"),            # Короткое имя
    ("Ivan", -5, "test@mail.com"),         # Отрицательный возраст
    ("Ivan", 25, "invalid_email"),         # Плохой email
])
def test_invalid_data(store, name, age, email):
    with pytest.raises(ValueError):
        store.add_user(name, age, email)