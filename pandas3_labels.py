import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])   # x=1, y=7, z=2

print(myvar)