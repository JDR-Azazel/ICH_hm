"""
Создайте класс Person, представляющий человека.
- Каждый человек должен иметь имя.
- Добавьте метод introduce(), который выводит приветствие с именем.

Пример вывода:
Hello, my name is Alice.
"""

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}.")

person1 = Person("Alice")
person1.introduce()

"""
На основе класса Person создайте класс Student.
- Студент должен иметь имя и номер курса.
- Метод introduce() должен сначала выводить базовое приветствие, а затем строку: I'm on course <номер_курса>.

Пример вывода:
Hello, my name is Alice.
I'm on course 2.
"""

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}.")


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def introduce(self):
        super().introduce()
        print(f"I'm on course {self.course}.")

student1 = Student("Alice", 2)
student1.introduce()

"""
На основе класса Person создайте класс Teacher.
- У преподавателя есть имя и предмет.
- Метод introduce() должен выводить имя и предмет.
- Метод introduce() должен выводить строку: Hello, I am professor <имя>. My subject is <предмет>.
- Создайте список, в котором будут Student и Teacher, и вызовите у всех метод introduce().

Пример вывода: 
Hello, my name is Alice.
I'm on course 2.
Hello, I am professor Bob. 
My subject is Mathematics
"""

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}.")


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def introduce(self):
        super().introduce()
        print(f"I'm on course {self.course}.")


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def introduce(self):
        print(f"Hello, I am professor {self.name}.")
        print(f"My subject is {self.subject}.")


people = [
    Student("Alice", 2),
    Teacher("Bob", "Mathematics")
]

for person in people:
    person.introduce()
