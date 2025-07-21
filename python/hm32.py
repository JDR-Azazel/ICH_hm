"""
Создайте функцию make_rounder(), которая принимает количество знаков для округления и возвращает другую функцию.
Полученная функция должна принимать число и возвращать его, округлённое до указанного ранее количества знаков после запятой.

Пример вызова:
print(round2(3.14159))
print(round2(2.71828))
print(round0(9.999))

Пример вывода:
3.14
2.72
10.0
"""

def make_rounder(precision_level):
    def round_engine(value):
        return round(value, precision_level)
    return round_engine

round_to_2 = make_rounder(2)
round_to_0 = make_rounder(0)

print(round_to_2(3.14159))
print(round_to_2(2.71828))
print(round_to_0(9.999))

"""
Создайте функцию, которая возвращает вложенный логгер событий.
Каждый вызов логгера должен сохранять событие с текущим временем (если оно передано) и возвращать весь список событий.

Пример вызова: 
log("Загрузка данных")
log("Обработка завершена")
log("Сохранение файла")

for event in log():
    print(event)

Пример вывода: 
Загрузка данных: 2025-03-24 14:06:29
Обработка завершена: 2025-03-24 14:06:29
Сохранение файла: 2025-03-24 14:06:29
"""

from datetime import datetime

def create_logger():
    log_storage = []

    def event_logger(message=None):
        if message:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_storage.append(f"{message}: {timestamp}")
        return log_storage

    return event_logger

log = create_logger()

log("Загрузка данных")
log("Обработка завершена")
log("Сохранение файла")

for entry in log():
    print(entry)

"""
Создайте декоратор frame, который оборачивает результат функции рамкой из 50 символов -, выводя по строке до и после 
вызова функции.

Пример декорируемой функции: 
def say_hello():
    print("Привет, игрок!")

Пример вывода: 
--------------------------------------------------
Привет, игрок!
--------------------------------------------------
"""

def frame(func):
    def wrapper():
        print("-" * 50)
        func()
        print("-" * 50)
    return wrapper

@frame
def say_hello():
    print("Привет, игрок!")

say_hello()

