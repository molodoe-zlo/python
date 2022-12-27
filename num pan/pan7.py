#На вход подается DataFrame из 3-х колонок дата рождения и смерти человека на русском языке в формате представленом ниже:
#Имя	Дата рождения	Дата смерти
#0	Никола Тесла	10 июля 1856 г.	7 января 1943 г.
#1	Альберт Эйнштейн	14 марта 1879 г.	18 апреля 1955 г.
#Необходимо вернуть исходную таблицу с добавленным в конце столбцом полных лет жизни.
#0	Никола Тесла	10 июля 1856 г.	7 января 1943 г.	86
#1	Альберт Эйнштейн	14 марта 1879 г.	18 апреля 1955 г.	76
#Формат даты единый, исключений нет, пробелы мужду элементами дат присутствуют, исключений (Nan) нету.
#P.S. Для обработки высокосных годов используйте модуль dateutil.relativedelta.
import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta

def end(df):
    birth = make_form(df["Дата рождения"])
    death = make_form(df["Дата смерти"])
    years = relativedelta(death, birth).years
    return years
  
def make_form(data):
    months = {"января": '01', 
            "февраля": '02', 
            "марта": '03', 
            "апреля": '04', 
            "мая":'05', 
            "июня":'06', 
            "июля":'07', 
            "августа": '08', 
            "сентября":'09',
            "октября":'10', 
            "ноября":'10', 
            "декабря":'12'}
    new_date = data.split(" ")
    res = [int(new_date[2]), int(months[new_date[1]]), int(new_date[0])]
    return (datetime.date(res[0], res[1], res[2]))

def rus_feature(df: pd.DataFrame) -> pd.DataFrame:
  df["Полных лет"] =  df.apply(end, axis=1)
  return df

names = pd.DataFrame({'Имя':['Никола Тесла'], 
                   'Дата рождения':['1 января 2000 г.'],
                   'Дата смерти':  ['31 декабря 2000 г.']})

print(rus_feature(names))