# Pandas is a Python library used for working with data sets.
# It has functions for analyzing, cleaning, exploring, and manipulating data.
# The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis"

import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)   # DataFrame is a 2 dimensional data structure,
                                      # like a 2 dimensional array, or a table with rows and columns

print(myvar)


# output:
#    cars  passings
# 0  BMW         3
# 1  Volvo         7
# 2  Ford         2