# Checking how many dimensions the arrays have- using ndim

import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)   # 0
print(b.ndim)   # 1
print(c.ndim)   # 2
print(d.ndim)   # 3