# We'll use append() function to insert an element and 'del' statement to delete an element.

numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("List= ", numList)

numList[5] = 600
print("List after updation = ", numList)

numList.append(111)
print("List after appending a value = ", numList)

del numList[1]      # You can also delete like this:    del numList[2:4]    del numList
print("List after deleting a value= ", numList)


