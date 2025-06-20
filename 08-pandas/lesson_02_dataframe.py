# import pandas as pd
#
# data = {
#     'Ism': ['Sobirjon', 'Maftuna', 'Anvar'],
#     'Yosh': [20, 21, 19],
#     'Shahar': ['Toshkent', 'Farg‘ona', 'Namangan']
# }
#
# df = pd.DataFrame(data)
#
#
# # print(df['Ism'])          # Faqat ism ustunini olish
# # print(df.loc[1])          # 2-qatordagi barcha ma’lumot
# # print(df['Yosh'].mean())  # O‘rtacha yosh
#
# print(df)

# -------------------- homework --------------------

import pandas as pd

data = {
    'Ism': ['Sobirjon', 'Maftuna', 'Anvar', 'Nodir'],
    'Yosh': [20, 21, 19, 22],
    'Shahar': ['Toshkent', 'Farg‘ona', 'Namangan', 'Samarqand'],
}

df = pd.DataFrame(data)

print(df['Yosh'].min())  # O‘rtacha yosh
print(df['Yosh'])  # Yosh ustunidagi barcha ma’lumotlar

df.to_csv('files/yangi_talabalar.csv', index=False)
