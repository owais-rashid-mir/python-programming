name = input("Enter your name:")
age = input("Enter your age:")

print("Name= ", name, "\nAge=", age)

n1 = input("Enter a number:")
n2 = input("Enter another number:")
print("Sum= ", n1+n2)   # It doesn't add the numbers, it concatenates them. This is because
                        # input() function takes user's input as a string.
                        #So, we need to use type-casting. Check the below snippet:


n3 = int(input("Enter a number:"))
n4 = int(input("Enter another number:"))
print("Sum= ", n3+n4)   # This will add the numbers

piVal = float(input("Enter value of PI:"))
print(piVal)