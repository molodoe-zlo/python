#Реализуйте функцию, принимающую на вход непустой тензор (может быть многомерным)
#и некоторое число  и возвращающую ближайший к числу элемент тензора. 
#Если ближайших несколько - выведите минимальный из ближайших. (Вернуть нужно само число, а не индекс числа!)
import numpy as np
import copy

def nearest_value(X: np.ndarray, a: float) -> float:
  af = X.astype(int)
  new_matrix = af.flatten()
  last = np.sort(new_matrix)
  index = (np.abs(last - a)).argmin()
  return (last[index])

X = np.array([[ 1,  2, 13],
              [15,  6,  8],
              [ 7, 18,  9]])
a = 7.2

print(nearest_value(X, a))