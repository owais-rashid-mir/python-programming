i = 0
while i <= 10:      # You can also use a bracket like:  while(i <= 10):
    print(i)
    i = i + 1   # There are no increment and decrement operators(i++, i--, ++i, --i) in Python)

print("\n")

# The above loop prints 0-10 but with a newline by default. If you want to print numbers in the same
# line separated by a space, tab etc, use 'end' keyword.
j = 0
while j <= 10:
    print(j, end=" ")       # or, you can write:    end=""   ,   end="\t"
    j = j + 1
