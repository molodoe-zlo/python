#В этой задаче на вход подаются всем известные данные о погибших/выживших пассажирах на титанике. 
#Сделать сводную таблицу по медианному возрасту для пола и класса. 
#Для примера посмотрите сводную таблицу по сумме выживших, для пола и класса.
import pandas as pd
from numpy import median
from pandas import MultiIndex

def age_stat(df: pd.DataFrame) -> pd.DataFrame:
    female = df[df['Sex'] == 'female']
    female1 = (female.loc[df['Pclass'] == 1])
    female1 = female1['Age'].dropna(axis=0)
    female2 = (female.loc[df['Pclass'] == 2])
    female2 = female2['Age'].dropna(axis=0)
    female3 = (female.loc[df['Pclass'] == 3])
    female3 = female3['Age'].dropna(axis=0)

    male = df[df['Sex'] == 'male']
    male1 = (male.loc[df['Pclass'] == 1])
    male1 = male1['Age'].dropna(axis=0)
    male2 = (male.loc[df['Pclass'] == 2])
    male2 = male2['Age'].dropna(axis=0)
    male3 = (male.loc[df['Pclass'] == 3])
    male3 = male3['Age'].dropna(axis=0)

    arrays = [ ['female', 'female', 'female', 'male', 'male', 'male'],
               ['1', '2', '3', '1', '2', '3'],
               [int(median(female1)), int(median(female2)), int(median(female3)), int(median(male1)), int(median(male2)), int(median(male3))] ]
    arrays = MultiIndex.from_arrays(arrays)
    return arrays

df = pd.read_csv('titanic_train.csv', index_col='PassengerId')

print(age_stat(df))