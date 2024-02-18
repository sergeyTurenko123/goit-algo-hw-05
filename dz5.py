# завдання 1
def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        if n < 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
    return fibonacci
    
number = caching_fibonacci()
print(number(15))
print(number(10))


# завдання 2
import re
from typing import Callable
from decimal import Decimal, getcontext
getcontext().prec = 6

def generator_numbers(text: str):
    numbers = re.findall(pattern= r"(\d+\.\d+)", string= text) # Знаходження цифр
    for number in numbers:
        yield(number ) # Вивід кожного числа окремо

def sum_profit(text: str, operation: Callable):    # виклик программи generator_numbers
    number = sum(map(Decimal, operation(text))) # Сумірування знайдених чисел. десятичне число
    return number

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers) # Виклик функції sum_profit з результатом generator_numbers
print(f"Загальний дохід: {total_income}")

