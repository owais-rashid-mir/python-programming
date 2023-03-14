import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x1 = np.where(arr == 4) 	# Finding the indexes where the value is 4

x2 = np.where(arr%2 == 0)	# Finding the indexes where the values are even

x3 = np.where(arr%2 == 1)	# Finding the indexes where the values are odd

print(x1)
print(x2)
print(x3)