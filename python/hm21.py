"""
Реализуйте функцию, которая принимает текст и возвращает словарь с подсчётом количества каждой буквы, игнорируя регистр
Данные: text = "Programming is fun!"
Пример вывода:
{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}
"""
from collections import Counter

text = "Programming is fun!".lower()

def word_counter(txt): # Metod 1
    return Counter(txt)

def word_counter2(txt): # Metod 2
    tmp = {}
    for i in txt:
        if i.isalpha():
            if i in tmp:
                tmp[i] += 1
            else:
                tmp[i] = 1
    return tmp

print(word_counter(text))
print(word_counter2(text))

"""
Создайте структуру для группировки студентов по классам. Добавьте студентов в соответствующие группы.
Данные: students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
Пример вывода:
{'class1': ['Alice', 'Charlie'], 'class2': ['Bob'], 'class3': ['Daisy']}
"""

students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
result = {}

for cls, name in students:
    if cls not in result:
        result[cls] = []
    if cls == "class1":
        result[cls].append(name)
    elif cls == "class2":
        result[cls].append(name)
    else:
        result[cls].append(name)

print(result)