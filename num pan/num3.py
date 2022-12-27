#Даны трехмерный тензор размерности X, состоящий из 0 или 1, или n картинок k*k. 
#Нужно применить к нему указанную маску размерности k*k.
#В случае, если биты в маске и картинке совпадают, то результирующий бит должен быть равен 0, иначе 1.
import numpy as np

def tensor_mask(X: np.ndarray, mask: np.ndarray) -> np.ndarray:
  newarr = np.logical_xor(X, mask)
  answer = np.where(newarr == True, 1, 0)
  return answer

X = np.array([
              [[ 1, 0, 1],
               [ 1, 1, 1],
               [ 0, 0, 1]],

              [[ 1, 1, 1],
               [ 1, 1, 1],
               [ 1, 1, 1]]
            ])
mask = np.array([[1, 1, 0],
                 [1, 1, 0],
                 [1, 1, 0]])

print(tensor_mask(X, mask))
