from pickle import FALSE
from xlsx2csv import Xlsx2csv
from io import StringIO
import pandas as pd

def read_excel(path: str, sheet_name: str) -> pd.DataFrame:
    buffer = StringIO()
    Xlsx2csv(path, outputencoding="utf-8", sheet_name=sheet_name).convert(buffer)
    buffer.seek(0)
    df = pd.read_csv(buffer)
    return df

df = read_excel('Dummy 0.xlsx', 'Sheet1')
#Drop Index
df.drop(columns  = df.columns[0], axis =1, inplace = True)

#Remove first row
# df = df.iloc [1:]

print(df.shape)
df.to_csv('convert.csv', header = False, index=False)