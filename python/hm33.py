"""
Создайте декоратор measure_time, который измеряет и выводит среднее время выполнения функции за 5 вызовов.
Функция может быть любой: например, сортировка списка, чтение из файла или расчёты.

Пример применения:
@measure_time
 def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

Пример вывода:
Среднее время выполнения для 5 вызовов:
0.21 секунд
Результат: 49999995000000
"""

import time
from functools import wraps

def measure_time(proto_func):
    @wraps(proto_func)
    def execution_unit(*args, **kwargs):
        execution_cycles = 5
        cycle_durations = []
        computation_result = None
        for cycle in range(execution_cycles):
            t_start = time.perf_counter()
            computation_result = proto_func(*args, **kwargs)
            t_end = time.perf_counter()
            cycle_durations.append(t_end - t_start)
        avg_duration = sum(cycle_durations) / execution_cycles
        print(f"Среднее время выполнения за {execution_cycles} циклов:\n{avg_duration:.6f} секунд")
        print(f"Результат: {computation_result}")
        return computation_result
    return execution_unit

@measure_time
def calculate_pi(precision_level=1_000_000):
    accumulator = 0.0
    for iteration_index in range(precision_level):
        term = (-1) ** iteration_index / (2 * iteration_index + 1)
        accumulator += term
    return accumulator * 4

# Вызов вычислительного модуля
calculate_pi()

"""
Доработайте декоратор measure_time, чтобы он принимал параметр repeats — количество вызовов функции.
Декоратор должен выполнять функцию указанное число раз и выводить среднее время выполнения.

Пример применения: 
@measure_time(10)
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

Пример вывода: 
Среднее время выполнения для 10 вызовов: 
0.21 секунд
Результат: 49999995000000
"""

def measure_time(repeats):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            durations = []
            result = None
            for _ in range(repeats):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                end = time.perf_counter()
                durations.append(end - start)
            average = sum(durations) / repeats
            print(f"Среднее время выполнения для {repeats} вызовов:\n{average:.2f} секунд")
            print(f"Результат: {result}")
            return result
        return wrapper
    return decorator

@measure_time(10)
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

compute()
