"""
Создайте класс Rectangle, который описывает прямоугольник.
- У каждого объекта должны быть два поля: width и height.
- Добавьте метод get_area(), который возвращает площадь прямоугольника.
- Создайте объект прямоугольника с произвольными значениями.
- Выведите его площадь.
- Измените ширину и высоту.
- Выведите новую площадь.

Пример вывода:
Площадь: 20
Новая площадь: 35
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

rect = Rectangle(2.223, 9)

print("Площадь:", rect.get_area())

rect.width = 7
rect.height = 5

print("Новая площадь:", rect.get_area())

"""
Реализуйте класс Counter, который представляет собой простой счётчик.
- Счётчик должен начинаться с нуля.
- Предусмотрите методы для увеличения и уменьшения значения на единицу, при этом при каждой операции должно отображаться новое значение счётчика.
- Добавьте метод, возвращающий текущий результат.
- Проверьте работу счётчика, выполнив несколько операций.

Значение увеличено, текущее: 1
Значение увеличено, текущее: 2
Значение увеличено, текущее: 3
Значение уменьшено, текущее: 2
Текущее значение: 2
"""

class Counter:
    def __init__(self):
        self.value = 0  # Счётчик начинается с нуля

    def increment(self):
        self.value += 1
        print(f"Значение увеличено, текущее: {self.value}")

    def decrement(self):
        self.value -= 1
        print(f"Значение уменьшено, текущее: {self.value}")

    def get_value(self):
        print(f"Текущее значение: {self.value}")
        return self.value

counter = Counter()
counter.increment()
counter.increment()
counter.increment()
counter.decrement()
counter.get_value()
