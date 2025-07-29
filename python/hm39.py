"""
Создайте абстрактный класс Shape.
- В классе должен быть метод area(), который возвращает площадь фигуры.
- Реализуйте два класса:
    - Circle, который принимает радиус.
    - Rectangle, который принимает ширину и высоту.
"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом.")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius})"

class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть положительными числами.")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

shapes = [Circle(3), Rectangle(4, 5)]
for shape in shapes:
    print(f"{shape} — Area: {shape.area():.2f}")

"""
Доработайте фигуры:
- Добавьте проверку в конструкторы Circle и Rectangle, чтобы значения были положительными.
- Если передано отрицательное или нулевое значение, выбрасывайте пользовательское исключение InvalidSizeError.
"""

class InvalidSizeError(Exception):
    pass

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise InvalidSizeError("Радиус должен быть положительным числом.")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius})"

class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise InvalidSizeError("Ширина и высота должны быть положительными числами.")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

shapes = [Circle(3), Rectangle(4, 5)]

for shape in shapes:
    print(f"{shape} — Area: {shape.area():.2f}")

try:
    bad_circle = Circle(-2)
except InvalidSizeError as e:
    print(f"Ошибка: {e}")

try:
    bad_rect = Rectangle(0, 5)
except InvalidSizeError as e:
    print(f"Ошибка: {e}")
