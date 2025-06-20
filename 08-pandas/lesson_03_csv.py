import pandas as pd

df = pd.read_csv('files/talabalar.csv')

# print(df.head())           # Yuqoridan 5 ta
# print(df.tail(2))          # Oxirgi 2 ta
# print("Shape:", df.shape)  # Qator va ustun soni
# print("Columns:", df.columns)
# print(df.describe())       # Statistika

print(df[['Ism', 'Yosh']] )