# Making a copy, changing the original array, and displaying both arrays.
# Copy is a new array, and the View is just a view of the original array.
# changes made to the copy will not affect original array.

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)


# Output:
# 42  2  3  4  5]
# [1 2 3 4 5]