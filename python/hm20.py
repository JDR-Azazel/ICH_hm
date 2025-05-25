"""
Напишите функцию, которая проверяет, является ли число n простым (делится только на 1 и само себя) и возвращает булевый
результат. Данные: n = 17
Пример вывода:
Число 17 является простым
"""

def simple_complex(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = 17
result = simple_complex(n)

if result:
    print(f"Число {n} является простым")
else:
    print(f"Число {n} не является простым")

"""
Напишите функцию, которая принимает filter_type ("even" или "odd") и произвольное количество чисел, возвращая только те,
которые соответствуют фильтру.
Пример вызова:
print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))

Пример вывода:
[2, 4, 6]
[15, 25]
Некорректный фильтр
"""

def filter_numbers(filter, *n):
    tmp = []
    if filter == "even":
        for i in n:
            if i %2 == 0:
                tmp.append(i)
        return tmp
    elif filter == "odd":
        for i in n:
            if i %2 != 0:
                tmp.append(i)
        return tmp
    else:
        return "Некорректный фильтр"


print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))

"""
Напишите функцию, которая принимает любое количество словарей и объединяет их в один. Если ключи повторяются, 
используется значение из последнего словаря.
Данные:
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}

Пример вызова:
print(merge_dicts(dict1, dict2, dict3))

Пример вывода:
{'a': 1, 'b': 3, 'c': 4, 'd': 5}
"""

def merge_dicts(*dict):
    tmp = {}
    for i in dict:
        tmp.update(i)
    return tmp

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}

print(merge_dicts(dict1, dict2, dict3))