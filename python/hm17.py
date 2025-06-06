"""
Напишите программу, которая проверяет, содержит ли первое множество все элементы второго множества. Реализуйте решение
несколькими способами. Решите одним из способов не используя возможности множеств.
Данные: set1 = {1, 2, 3, 4} set2 = {2, 3}
Пример вывода: True
"""

set1 = {1, 2, 3, 4}
set2 = {2, 3}

# VAR 1

set3 = []

for i in set1:
    if i in set2:
        set3.append(i)

print(len(set2) == len(set3))

# VAR 2

print("True" if len(set1 & set2) != 0 else "False")

"""
Напишите программу, которая проверяет, являются ли элементы одного из множеств подмножеством другого. В случае 
положительного ответа возвращает разницу между двумя множествами. Проверить необходимо в обе стороны.
Данные: set1 = {2, 3, 4, 5, 6} set2 = {4, 5} 
Пример вывода: 
Подмножество: True 
Разница: {2, 3, 6}
"""

set1 = {2, 3, 4, 5, 6}
set2 = {4, 5}

print(f"Подмножество: {"True" if set1.issubset(set2) or set2.issubset(set1) else "False"}\nРазница: {set1 - set2}")

