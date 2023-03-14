# Converting the following 1-D array with 12 elements into a 2-D array with 4 rows and 3 columns.

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)