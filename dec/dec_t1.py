import functools
import random
from typing import List

# Модифицируйте код декоратора reverse_string
def reverse_string(func):
    """Если результат функции - строка, то ее нужно перевернуть. Иначе вернуть None."""
    @functools.wraps(func)
    def wrapper():
        a = func()
        if type(a) == str:
            return a[::-1]
        else: 
            return None 
    return wrapper


@reverse_string
def get_university_name():
    return "Western Institute of Technology and Higher Education"

@reverse_string
def get_university_founding_year() :
    return 1957

# вывод для примера
print(
    get_university_name(),
    get_university_founding_year(),
    sep="\n"
)