import pandas as pd

file_path = "cbsas.csv"
df = pd.read_csv(file_path)

print(df.head())