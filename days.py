# генератор с именем gendates и параметрами month, day, year, 
# который позволит генерировать последовательные даты, 
# начинающиеся с заданного месяца, дня, года.
import calendar
def gendates(month, day, year):
    i = [month, day, year]
    while True:
        yield i
        if i[1] == calendar.monthrange(i[2],i[0])[1]:
            i[1] = 0
            i[0] += 1
        if i[0] > 12:
            i[0] = 1
            i[2] += 1 
        i[1] += 1

# a = gendates(12, 5, 2022)
# for  i in range(365):
#     print(next(a))



# генератор с именем gendow и параметрами month, day, year, 
# который будет генерировать последовательные дни недели (в виде строк), 
# начинающиеся с данного месяца, дня, года. 
def gendow (month, day, year):
    weekday = {
        0:'ПН',
        1:'ВТ',
        2:'СР',
        3:'ЧТ',
        4:'ПТ',
        5:'СБ',
        6:'ВС'
    }
    a = gendates(month, day, year)
    arr = []
    while True:
        arr = next(a)
        y = arr[2]
        m = arr[0]
        d = arr[1]
        yield weekday[calendar.weekday(y, m, d)]

# a = gendow(10, 21, 2020)
# for  i in range(10):
#     print(next(a))
#кошачьиправки 0-7ззззззззззззззззз
#кошачьиправки ееееееееееееееееееееееееееееееееее6



# генератор, которая вернет результат gendates и gendow в виде кортежа (день, месяц, год, день недели)
def beautifulday(month, day, year):
    date = gendates(month, day, year)
    week = gendow(month, day, year)
    arr = []
    while True:
        arr.append(next(date))
        arr.append(next(week))
        yield tuple(arr)
        arr.clear()

a = beautifulday(10, 21, 2020)
for  i in range(10):
    print(next(a))