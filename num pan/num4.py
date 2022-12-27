#На вход подается np.ndarray c натуральными числами. Надо получить массив сумм цифр в этих числах.
import numpy as np

def num_sum(a: np.ndarray) -> np.ndarray:
  k = a // 10 ** np.arange(len(str(np.max(a))))[:, None] % 10
  answer = np.sum(k, axis = 0)
  return answer

a = np.array([1241, 354, 121])
print(num_sum(a))