"""
Напишите функцию, которая выполняет деление двух чисел, введенных пользователем, и обрабатывает возможные ошибки.
Пример вывода:
Введите делимое: 345
Введите делитель: 5a
Ошибка: Введено некорректное число.
"""
import logging

logging.basicConfig(
    filename="errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s"
)

def num_divisor():
    try:
        num = float(input("Введите делимое: "))
        divisor = float(input("Введите делитель: "))
        result = num / divisor
        print(f"Результат: {result}")
    except ValueError:
        print("Ошибка: Введено некорректное число.")
        logging.error("Ошибка: Введено некорректное число.")
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль невозможно.")
        logging.error("Ошибка: Деление на ноль невозможно.")

num_divisor()

"""
Перенаправьте в предыдущей задаче вывод ошибок в файл errors.log в соответствии с форматом ниже.
Пример вывода:
2025-02-23 22:38:53,686 - ERROR - test.py - 16 - Ошибка: Введено некорректное число.
"""





