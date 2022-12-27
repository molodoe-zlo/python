#Дан одномерный массив целых чисел. Необходимо отсортировать в нем только числа, которые делятся на 2. 
#При этом начальный массив изменять нельзя.
import numpy as np
import copy

def sort_evens(A: np.ndarray) -> np.ndarray:
  newarr = A[A%2 == 0]
  newarr = np.sort(newarr)
  return newarr

A = np.array([8, 9, 5, 12, 4, 10, 6, 2])

print(sort_evens(A))