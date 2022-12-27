import pandas as pd
import numpy as np
def age_table(df: pd.DataFrame) -> pd.DataFrame:
    return pd.pivot_table(df, values='Age', index=['Sex', 'Pclass'], aggfunc=np.median)

if __name__ == '__main__':
    df = pd.read_csv('titanic_train.csv', index_col='PassengerId')
    age_table(df)