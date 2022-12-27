import functools
import random
from typing import List
from math import sqrt

# Модифицируйте код декоратора prime_filter
def prime_filter(func):
    """Дан список целых чисел, возвращайте только простые целые числа"""
    @functools.wraps(func)
    def wrapper(from_num, to_num):
        primes = []
        for i in range(from_num, to_num):
            for j in range(2, i):
                if (i % j == 0):
                    break
                elif j > int((sqrt(i)) + 1):
                    primes.append(i)
                    break
        return primes
    return wrapper

@prime_filter
def numbers(from_num, to_num):
    return [num for num in range(from_num, to_num)]

# вывод для примера
print(numbers(from_num=2, to_num=20)) 
