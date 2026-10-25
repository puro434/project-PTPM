import re

class UserStore:
    def __init__(self):
        self.users = {}
        self._next_id = 1

    def add_user(self, name, age, email):
        # Валидация
        if not name or len(name) < 2:
            raise ValueError("Имя слишком короткое")
        if not (0 < age < 120):
            raise ValueError("Некорректный возраст")
        if not re.match(r"^[\w.+-]+@[\w-]+\.[\w.-]+$", email):
            raise ValueError("Некорректный email")
        
        uid = self._next_id
        self.users[uid] = {"id": uid, "name": name, "age": age, "email": email}
        self._next_id += 1
        return uid

    def get_user(self, uid):
        return self.users.get(uid)

    def get_all_users(self):
        return list(self.users.values())

    def delete_user(self, uid):
        if uid in self.users:
            del self.users[uid]