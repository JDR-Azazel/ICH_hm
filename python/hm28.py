"""
Напишите программу, которая помогает планировать дела.
Программа должна бесконечно выводить план на следующий день недели, пока пользователь нажимает 'Enter'.

Пример ввода:
Нажмите 'Enter' для получения плана:
Monday: Gym, Work, Read book
Нажмите 'Enter' для получения плана:
Tuesday: Meeting, Work, Study Python
...
Нажмите 'Enter' для получения плана:
Sunday: Family time, Rest
Нажмите 'Enter' для получения плана:
Monday: Gym, Work, Read book
Нажмите 'Enter' для получения плана: q
...
"""
from itertools import cycle, product

# Расписание дел на неделю
weekly_schedule = {
    "Monday": ["Gym", "Work", "Read book"],
    "Tuesday": ["Meeting", "Work", "Study Python"],
    "Wednesday": ["Shopping", "Work", "Watch movie"],
    "Thursday": ["Work", "Call parents", "Play guitar"],
    "Friday": ["Work", "Dinner with friends"],
    "Saturday": ["Hiking", "Rest"],
    "Sunday": ["Family time", "Rest"]
}

week_days = list(weekly_schedule.keys())

day_cycle = cycle(week_days)

while True:
    user_input = input("Нажмите 'Enter' для получения плана (или 'q' для выхода): ")
    if user_input.lower() == 'q':
        print("Завершения программы")
        break
    day = next(day_cycle)
    tasks = ', '.join(weekly_schedule[day])
    print(f"{day}: {tasks}")

"""
Напишите функцию, которая принимает несколько списков с названиями продуктов и возвращает генератор, содержащий все 
продукты в нижнем регистре. Выведите содержимое генератора.

Пример вывода:
apple
banana
orange
carrot
tomato
cucumber
milk
cheese
yogurt
"""

fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]

def gen_all_prod(*lists):
    return (item.lower() for lst in lists for item in lst)

all_products = gen_all_prod(fruits, vegetables, dairy)

for product in all_products:
    print(product)


"""
Напишите функцию, которая принимает списки типов одежды, цветов и размеров, а затем генерирует все возможные комбинации
в формате "Clothe - Color - Size".
Пример вывода:
T-shirt - Red - S
T-shirt - Red - M
T-shirt - Red - L
T-shirt - Blue - S
...
Jacket - Black - L
"""

clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

def all_var_gen(clothes, colors, sizes):
    return (f"{c} - {color} - {size}" for c, color, size in product(clothes, colors, sizes))

for variant in all_var_gen(clothes, colors, sizes):
    print(variant)




