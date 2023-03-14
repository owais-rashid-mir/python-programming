list1 = [ [1, 2, 3], [4, 5, 6] ]
tuple1 = ( (1, 2), (3), (4, 5, 6) )

print(list1)
print(tuple1)

print("Values in list1 by row are: ")
for row in list1:
    for item in row:
        print(item)
    print()
