#Реализуйте функцию, которая во входной вещественной матрице X находит все значения nan и заменяет их 
#на медиану остальных элементов столбца. Если все элементы столбца матрицы nan, то заполняем столбец нулями.
import numpy as np

def replace_nans(X: np.ndarray) -> np.ndarray:
  newarr = np.nanmedian(X, axis = 0)
  answer = np.where(np.isnan(X), np.nan_to_num(newarr), X)
  return answer

X = np.array([[np.nan,      4,  np.nan],
              [np.nan, np.nan,       8],
              [np.nan,      5,  np.nan]])

print(replace_nans(X))