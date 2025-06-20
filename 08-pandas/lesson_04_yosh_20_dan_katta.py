import pandas as pd

df = pd.read_csv('files/talabalar.csv')

print(df['Ism'])  # Faqat ism ustunini olish
print(df['Yosh'].max())  # Katta yosh
print(df['Yosh'].mean())  # O‘rtacha yosh

print(df.describe())

df = df[df['Yosh'] > 20]

df.to_csv('files/talabalar_yosh_20_dan_katta.csv', index=False)
