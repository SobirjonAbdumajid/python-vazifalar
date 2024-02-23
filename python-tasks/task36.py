"""
Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.

"""

# buyurtmalar = []

# print('Nima buyurtirasiz: ')
# n = 1
# while True:
#     buyurtmalar.append(input(f'{n}-buyurtma: '))
#     n+=1
#     if 'enough' in buyurtmalar:
#         break
# print('Sizning buyurtmalaringiz:')

# del buyurtmalar[-1]

# for buyurtma in buyurtmalar:
#     print(f"{buyurtma},",end=' ')



savat =[]
while True:
    mahsulot = input("Savatga mahsulot qo'shing:")
    savat.append(mahsulot)
    javob = input("Yana mahsulot qo\'shasizmi?(ha/yo\'q)")
    if javob != 'ha':
        break