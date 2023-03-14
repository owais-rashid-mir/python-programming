from myPackage import mathOp, message, largest

message.messageFxn()

n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))

a = mathOp.addFxn(n1, n2)
print(a)
print("Difference= ", mathOp.subFxn(n1, n2))
print("Product= ", mathOp.mulFxn(n1, n2))
print("Division= ", mathOp.divFxn(n1, n2))
print("Remainder= ", mathOp.modFxn(n1, n2))
print("Quotient= ", mathOp.quotientFxn(n1, n2))
print("Average= ", mathOp.averageFxn(n1, n2))
print("Power= ", mathOp.powerFxn(n1, n2))

print("Largest= ", largest.largestFxn(n1, n2))

