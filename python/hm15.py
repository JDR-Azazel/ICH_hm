"""
Напишите программу, которая обрабатывает список из строк и удаляет все строки, содержащие более одного слова, а также
преобразует оставшиеся строки к нижнему регистру. Данные:
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
Пример вывода:
Обработанный список: ['hello', 'world', 'simple']
"""

text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
text = []
for i in text_list:
    if " " not in i:
        text.append(i.lower())

print("Обработанный список:",text)


"""
Дан список товаров с ценами. Программа должна применить скидку к каждому товару и добавить в список элемент с новой 
ценой. В конце вывести таблицу с новой ценой.Данные:
products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
Пример вывода:
Введите скидку (в процентах): 17

Товар          Старая цена    Новая цена
Laptop            1200.00$       996.00$
Mouse               25.00$        20.75$
Keyboard            75.00$        62.25$
Monitor            200.00$       166.00$
"""

usr_inp = int(input("Введите скидку (в процентах): "))
products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]

print(f"{"Товар":<10}{"Старая цена":<15}{"Новая цена"}")
for i in products:
    print(f"{i[0]:<10}{i[1]:>10.2f}${(100 - usr_inp) / 100 * i[1]:>13.2f}$")