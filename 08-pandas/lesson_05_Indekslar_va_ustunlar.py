import pandas as pd

data = {
    'Ism': ['Sobirjon', 'Maftuna', 'Anvar', 'Nodir'],
    'Yosh': [20, 21, 19, 22],
    'Shahar': ['Toshkent', 'Farg‘ona', 'Namangan', 'Samarqand']
}

df = pd.DataFrame(data)

# print(df['Ism'])         # bitta ustun
# print(df[['Ism', 'Yosh']])  # bir nechta ustun

# print(df.iloc[0])       # 1-qatordagi ma’lumot
# print(df.iloc[1:3])    # 2 va 3-qator

print(df.loc[0])            # index 0 bo‘lgan qator
# print(df.loc[df['Yosh'] > 20])  # 20 dan katta yoshdagilar

