# генератор, которые выводит простые числа
from math import sqrt
def  primenumbers(n):
    for i in range (2, int((sqrt(n)) + 1)):
        if (n % i == 0):
            break
    else:
        return 1

def gen_primenumbers():
    i = 1
    while True:
        if (primenumbers(i) == 1): 
            yield i
        i += 1

a = gen_primenumbers()
for i in range (20):
    print(next(a))