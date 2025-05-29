"""
Напишите рекурсивную функцию, которая находит сумму всех цифр числа. Пример вывода: 24
"""

num = 43197

def num_sum(n: int) -> int:
    if n == 0:
        return 0
    return n % 10 + num_sum(n // 10)

print(num_sum(num))

"""
Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках. Пример вывода: 28
"""

from typing import Union

nested_numbers = [1, [2, 3], [4, [5, 6]], 7]

def dep_sum(data: list[Union[int, list]]) -> int:
    total = 0
    for item in data:
        if isinstance(item, list):
            total += dep_sum(item)
        else:
            total += item
    return total

print(dep_sum(nested_numbers))
