# Program to check if a substring is present in a given string or not.

s = input("Enter a string : ")
subStr = input("Enter a word : ")

if s.find(subStr) == -1:
    print("Substring is not present in the string")

else:
    print("Substring is present in the string")