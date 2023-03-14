# Swapping 2 elements in a list

myList = [1, 2, 3, 4]
print("Before swapping: ", myList)

temp = myList[1]
myList[1] = myList[3]
myList[3] = temp

print("After swapping: ", myList)