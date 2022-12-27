#В этой задаче на вход подаются всем известные данные о погибших/выживших пассажирах на титанике.
#Выведите список имен незамужних женщин(Miss) отсортированный по популярности.
#В полном имени девушек имя - это первое слово без скобок после Miss.
#Остальные строки не рассматриваем.
#Девушки с одинаковой популярностью сортируются по имени в алфавитном порядке.
#Слово/имя - подстрока без пробелов. Популярность - количество таких имен в таблице.
import re
import pandas as pd
from collections import Counter

def fename_stat(df: pd.DataFrame) -> pd.DataFrame:
    r = r'Miss\. (?P<Name>[A-Za-z]+)'
    female = df[df['Name'].str.contains(r, regex=True)]['Name'].apply(lambda x: re.findall(r,x)[0])
    name = list(dict(Counter(female)).items())
    df1 = pd.DataFrame(name, columns = ['Name', 'Popularity'])
    df1 = df1.sort_values(by = ['Popularity', 'Name'], ascending=[0,1]).reset_index(drop=True)
    return df1

df = pd.read_csv('titanic_train.csv', index_col='PassengerId')

print(fename_stat(df))