"""
Создайте класс User, представляющий пользователя.
- При создании должны указываться логин (username) и пароль (password).
- У класса должно быть поле total_users, хранящее общее количество созданных пользователей.
- При каждом создании нового объекта User, счётчик должен увеличиваться.
- Добавьте метод get_total(), возвращающий количество пользователей.
- Проверьте, что счётчик работает.

Пример вывода:
Total users: 2
"""

class User:
    total_users = 0

    def __init__(self, username, password):
        self.username = username
        self.password = password
        User.total_users += 1

    def get_total(self):
        return User.total_users

user1 = User("Crusader3000", "abracadabra")
user2 = User("Marley", "don't_worry_be_happy")

print("Total users:", user2.get_total())

"""
Доработайте класс User.
- Добавьте валидации полей при создании.
- Имя должно быть непустой строкой.
- Пароль должен быть строкой длиной не менее 5 символов.
- Если данные некорректны — выбрасывайте ValueError.
- Добавьте строковое представление объекта.
- Проверьте работу класса с разными значениями.

Пример вызова: 
user1 = User("alice", "secret")
user2 = User("bob", "qwe")

Пример вывода: 
User: alice
...
ValueError: Invalid password: 
'qwe'.
"""

class User:
    total_users = 0

    def __init__(self, username, password):
        if not isinstance(username, str) or not username.strip():
            raise ValueError(f"Invalid username: '{username}'")

        if not isinstance(password, str) or len(password) < 5:
            raise ValueError(f"Invalid password: '{password}'")

        self.username = username
        self.password = password
        User.total_users += 1

    def get_total(self):
        return User.total_users

    def __str__(self):
        return f"User: {self.username}"

try:
    user1 = User("Crusader3000", "abracadabra")
    print(user1)
except ValueError as e:
    print("Ошибка:", e)

try:
    user2 = User("Marley", "be")
    print(user2)
except ValueError as e:
    print("Ошибка:", e)

print("Total users:", User.total_users)
