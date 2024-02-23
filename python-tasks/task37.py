"""
e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. 
Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.

"""

# e_bozor = {}
# n = 1

# while True:
#     mahsulotlar = input(f'{n}-mahsulotni nomini kiriting: ')
#     n += 1
#     if mahsulotlar.lower() == 'enough':
#         break
#     narx = input(f'{mahsulotlar}ning narxini kiriting: ')
#     e_bozor[mahsulotlar] = float(narx)

# print('\nSizning mahsulotlaringiz')
# for mahsulot, narx in e_bozor.items():
#     print(f'{mahsulot} -> {narx}')



mahsulotlar = {}
while True:
    mahsulot = input("Mahsulot nomini kiriting: ")
    narh = input(f"{mahsulot.title()}ning narhini kiriting: ")
    mahsulotlar[mahsulot] = narh
    javob = input("Yana mahsulot qo'shasizmi?(ha/yo'q)")
    if javob != 'ha':
        break