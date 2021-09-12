import pandas as pd
from openpyxl import Workbook

df = pd.read_csv('Names.csv', header=None)
df.columns = ['First', 'Last', 'Address', 'City','State','Area Code','Salary']

#print(df[['State','Area Code']])

#Print Slice of first 3 rows (indexed 0 to 2)
#print(df['First'][0:3])

print(df.iloc[1])