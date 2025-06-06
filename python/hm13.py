"""
Напишите программу, которая создаёт новый кортеж, состоящий из элементов изначального в том же порядке. Добавить в него
только элементы, которые больше всех предыдущих значений в исходном кортеже. Данные: numbers = (3, 7, 2, 8, 5, 10, 1)
Пример вывода:
Кортеж по возрастанию: (3, 7, 8, 10)
"""

numbers = (3, 7, 2, 8, 5, 10, 1)
value = (numbers[0],)
for i in numbers[1:]:
    if i > max(value):
        value += (i,)

print(value)

"""
Напишите программу, которая находит индексы элементов кортежа, встречающихся более одного раза.
Вывести сами элементы и их индексы. Данные: numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
Пример вывода:
Индексы элемента 2: 1 4 9 
Индексы элемента 3: 2 6 
Индексы элемента 4: 3 8
"""

numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)

for index, i in enumerate(numbers):
    if numbers.count(i) > 1 and numbers.index(i) == index:
        print(f"Индексы элемента {i}:", end= " ")
        for index_1, j in enumerate(numbers):
            if j == i:
                print(index_1, end=" ")
        print()


