import pandas as pd
df = pd.read_csv('cleaned_data.csv')

print(set(df['ShowerCount'].values.tolist()))