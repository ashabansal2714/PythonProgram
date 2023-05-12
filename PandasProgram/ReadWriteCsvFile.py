import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport
#Read csv file
df = pd.read_csv(r'C:/Users/Asha Bansal/OneDrive/Documents/Python/Python program/PandasProgram/zomato.csv')
print(df)
# Take uppr 2 values
print(df.head(2))
# Take lower two values
print(df.tail(2))
#Describe file numerical values
print(df.describe())
# write data in csv file
df["address"][0]="Bangalore"
df = df.to_csv('C:/Users/Asha Bansal/OneDrive/Documents/Python/Python program/PandasProgram//Zomato_Update.csv')

# Generate profile
profile = ProfileReport(df)
profile.to_file(Output_file = "zomato.html")