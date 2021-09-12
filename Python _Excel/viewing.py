import pandas as pd
from openpyxl import Workbook

df = pd.read_csv('Names.csv', header=None)
df.columns = ['First', 'Last', 'Address', 'City','State','Area Code','Salary']

print(df.columns)
