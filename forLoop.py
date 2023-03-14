# Prints 1-10.
# The 2nd argument of range() is 11, so one less than 11, i.e, up to 10 will be printed.
for i in range(1, 11):      # You can also write:    range(11)
    print(i, end=" ")

print("\n")

# By default in For loop, there is increment by 1. If you want to increment by a different number, use
# 3rd parameter(called as 'step') in the range().
for j in range(1, 11, 2):
    print(j, end=" ")