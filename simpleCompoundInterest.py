p = float(input("Enter the principal amount : "))
n = float(input("Enter the number of years : "))
r = float(input("Enter the rate of interest : "))

# calculate simple interest
si = (p * n * r) / 100
print("Simple interest : ", si)

# compute compound interest
ci = p * (pow((1 + r / 100), n))
print("Compound interest :", ci)
