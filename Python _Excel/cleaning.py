import pandas as pd
from openpyxl import Workbook
import numpy as np

df = pd.read_csv('Names.csv', header=None)
df.columns = ['First','Last','Address','City','State','Area Code','Income']

df.drop(columns='Address',inplace=True)

df = df.set_index('Area Code')

#print(df.loc[8074])
#print(df.iloc[0])

#print Split of results starting from Area Code/Index 8074..., & prints First name
#print(df.loc[8074:, 'First'])

#print(df.First.str.split(expand=True))

#Return the first index[0] of the Column first Name that is split on whitespace
df.First = df.First.str.split().str[0]
df = df.replace(np.nan, 'N/A', regex=True)

print(df)

to_excel = df.to_excel('modified.xlsx')