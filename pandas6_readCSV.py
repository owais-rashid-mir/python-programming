# A simple way to store big data sets is to use CSV files (comma separated files).
import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string())   # to_string() to print the entire DataFrame.