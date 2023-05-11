import numpy as np
import pandas as pd

df = pd.read_csv(r'C:/Users/Asha Bansal/OneDrive/Documents/Python/Python program/PandasProgram/zomato.csv')
print(df)
print(df.head(2))
print(df.tail(2))
print(df.describe())
df["address"][0]="Bangalore"
df = df.to_csv('C:/Users/Asha Bansal/OneDrive/Documents/Python/Python program/PandasProgram//Zomato_Update.csv')
