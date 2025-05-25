"""
 Напишите программу, которая получит два логических значения от пользователя и выведет результат
логических операций and, or, not для этих значений, а также сравнение на равенство и неравенство.
Для операции not используйте первое число. Продумайте в каком виде получать ввод от пользователя
для логического значения.
"""

# var 1

l1 = bool(int(input("input value 0 if False, 1 if True: ")))
l2 = bool(int(input("input value 0 if False, 1 if True: ")))

print("Операция с and, logic_val_1 and logic_val_2:", l1 and l2)
print("Операция с or, logic_val_1 or logic_val_2:", l1 or l2)
print("Операция с not, not logic_val_1: ", not l1)
print("Операция с равенством logic_val_1 == logic_val_2:", l1 == l2)
print("Операция с неравенством logic_val_1 != logic_val_2:", l1 != l2)



# var 2 знаю что доп балов за это не будет есть зачет и не зачет, но вот код)
# \n предусмотрены из эстетических соображений на случай запуска всего кода со всей домашкой

print("\nВведите пустые строки для завершения программы\n")

while True:

    a = input("Введите первое логическое значения a (True/False): ")
    b = input("Введите второе логическое значения b (True/False): ")

    if a.lower() == "true":
        a = True
    elif a.lower() == "false":
        a = False
    if b.lower() == "true":
        b = True
    elif b.lower() == "false":
        b = False
    else:
        print("\nBye,bye\n")
        break

    print("\nОперация с and, a and b:", a and b)
    print("Операция с or, a or b:", a or b)
    print("Операция с not, not a:", not a)
    print("Операция с равенством a == b:", a == b)
    print("Операция с неравенством a != b:", a != b, end="\n\n")

"""
Напишите программу, которая принимает на вход логические значения двух переменных
(свет включён и окно открыто) и проверяет: Оба ли условия выполнены. Хотя бы одно из условий выполнено.
Пример вывода:
Свет включён? True  
Окно открыто? False  
Оба условия выполнены? False  
Хотя бы одно условие выполнено? True
"""

light = bool(int(input("input value 0 if False, 1 if True: ")))
window = bool(int(input("input value 0 if False, 1 if True: ")))

condition_and = light and window
condition_or = light or window

print("\nСвет включён?", light, "\nОкно открыто?", window)
print("Оба условия выполнены?", condition_and, "\nХотя бы одно условие выполнено?", condition_or, end="\n\n")

"""
Напишите программу для расчёта стоимости использования мобильного тарифа: 
Базовая стоимость: 30 евро.
Каждый мегабайт интернета сверх 500 МБ стоит 0.2 евро.
Программа должна запросить у пользователя количество использованных мегабайтов и вывести сколько всего он заплатил 
(базовый и переплата). 
Пример вывода:
Введите использованные мегабайты: 510
Общая стоимость: 32.0
"""

# 1 var

price = 30
add_price = 0.2
base_mb = 500
used_mb = int(input("Введите использованные мегабайты: "))

extra_price = (used_mb - 500) * 0.2
total = price + (used_mb >= base_mb) * extra_price

print("Общая стоимость:", total, end="\n\n")

# 2 var

used_mb = int(input("Введите использованные мегабайты: "))
print("Общая стоимость:", 30 + (used_mb >= 500) * ((used_mb - 500) * 0.2))

