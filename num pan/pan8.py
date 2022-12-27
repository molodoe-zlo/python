#В этой задаче на вход подаются всем известные данные о погибших/выживших пассажирах на титанике. (Файл titanik_train.csv в папке data).
#Верните среднее, медиану, максимальное и минимальное значение возраста погибших мужчин. Именно в данном порядке.
import pandas as pd
import numpy as np

def men_stat(df: pd.DataFrame) -> float:
    male = df[df['Sex'] == 'male']
    male = male.loc[df['Survived'] == 0]
    male = male['Age'].dropna(axis=0)
    return (int(np.mean(male)), int(np.median(male)), int(np.max(male)), int(np.min(male)))

df = pd.read_csv('titanic_train.csv', index_col='PassengerId')

print(men_stat(df))