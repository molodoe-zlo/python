# Напишите декоратор retry: 
# декоратор вызовает функцию, которая возвращает True/False 
# для индикации успешного или неуспешного выполнения функции. 
# При сбое декоратор должен подождать и повторить попытку выполнения функции. 
# При повторных неудачах декоратор должен ждать дольше между каждой последующей попыткой. 
# Если у декоратора заканчиваются попытки, он сдается и возвращает исключение
import time

def retry(retries):
    def decorator(func):
        def retry_func(*arg, **kwarg):
            for k in range(retries):
                try:
                    func(*arg, **kwarg)
                    return True

                except:
                    time.sleep(k+1)
                    print(f'{k} retry')
                
            return Exception(f'{func.__name__} was failed with params {arg}, {kwarg}')
        return retry_func
    return decorator

#кошачьиправки Я;%55555552222222ЁЁЁЁЁЁЁЁЁЁЁЁ 7l7 l.t, FGU          KT yh,.......ikkkkk9mol

@retry(5)
def func():
    raise Exception

func()