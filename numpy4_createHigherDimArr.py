# defining the number of dimensions by using the ndmin argument.
import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)



# output:
# [[[[[1 2 3 4]]]]]     - 5 brackets specify 5D array
# number of dimensions : 5