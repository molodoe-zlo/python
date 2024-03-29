# Создать декоратор simple_decorator с "хорошим поведением", то есть 
# декоратор при котором происходит сохранение "магических" полей __name__  и  __doc__
# Должны проходиться тесты


def simple_decorator(func):
    def installing_doc_name(arg):       
        res = func(arg)
        res.__name__ = arg.__name__
        res.__doc__ = arg.__doc__
        return res
    return installing_doc_name

    
@simple_decorator
def my_simple_logging_decorator(func):
    def you_will_never_see_this_name(*args, **kwargs):
        print('calling {}'.format(func.__name__))
        return func(*args, **kwargs)
    return you_will_never_see_this_name

@my_simple_logging_decorator
def double(x):
    'Doubles a number.'
    return 2 * x

assert double.__name__ == 'double'
assert double.__doc__ == 'Doubles a number.'
print(double(155))