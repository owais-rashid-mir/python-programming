import numpy as np

arr1 = np.array(42)		# 0D array
arr2 = np.array([1, 2, 3, 4, 5])	# 1D array
arr3 = np.array([[1, 2, 3], [4, 5, 6]])		# 2D array
arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])	# 3D array

print(arr1)
print(arr2)
print(arr3)
print(arr4)

print(arr2[1])
print('2nd element on 1st row: ', arr3[0, 1])