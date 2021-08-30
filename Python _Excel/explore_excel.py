import pandas as pd
from openpyxl.workbook import Workbook

df_excel = pd.read_excel('regions.xlsx')
df_csv = pd.read_csv('Names.csv')
df_txt = pd.read_csv('data.txt')

print(df_excel)
