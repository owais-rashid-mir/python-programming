# Making a view, changing the original array, and displaying both arrays.
# changes made to the View will affect the original array

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)


# output:
# [42  2  3  4  5]
# [42  2  3  4  5]