# Modules- Arithmetic operations.

import moduleExample2

n1 = int(input("Enter a number:"))
n2 = int(input("Enter another number:"))

a = moduleExample2.add(n1, n2)
print('The sum is:', a)

b = moduleExample2.sub(n1, n2)
print('The difference is:', b)

c = moduleExample2.mul(n1, n2)
print('The product is:', c)

d = moduleExample2.div(n1, n2)
print('The division is:', d)

print('The remainder is:', moduleExample2.mod(n1, n2))

