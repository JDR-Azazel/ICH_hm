"""
У вас есть список заказов. Каждый заказ содержит название продукта и его цену. Напишите функцию, которая:
Отбирает заказы дороже 500.
Создаёт список названий отобранных продуктов в алфавитном порядке.
Возвращает итоговый список названий.

Пример вывода: ['Chair', 'Laptop']
"""

orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]

def order_choice(ord):
    tmp = list(filter(lambda x: x["price"]>500, ord))
    return sorted(map(lambda x: x["product"], tmp))

print(order_choice(orders))

"""
Дан список продаж в виде кортежей (товар, количество, цена). Напишите программу, которая:
Вычисляет общую выручку для каждого товара.
Возвращает словарь с товарами {товар: выручка}, отсортированный по убыванию выручки.
Пример вывода: {'Chair': 16000, 'Laptop': 6000, 'Monitor': 3000, 'Keyboard': 1500, 'Mouse': 1000}
"""

sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)
]

def sales_counter(list):
    return sorted(map(lambda x: (x[0], x[1] * x[2]), list), key=lambda x: -x[1])

print(sales_counter(sales))