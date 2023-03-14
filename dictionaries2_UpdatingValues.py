myDict = {'Name': 'Owais', 'Course': 'MCA', 'Rollno': '04'}

print(myDict)

myDict['Marks'] = 95    # Adding an item.
print("After adding an item: ", myDict)

myDict['Rollno'] = '05'     # Modifying an item
print("After modifying an item: ", myDict)

del myDict['Course']    # Deleting an item
print("After deleting an item: ", myDict)

myDict.clear()      # Deleting all the elements
print("After clear(), Dictionary has no items: ", myDict)
