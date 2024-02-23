'''
Yuqoridagi ikki dasturni jamlaymiz. 
Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). 
Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.

'''

# e_bozor = {}
# n = 1

# while True:
#     mahsulotlar = input(f'{n}-mahsulotni nomini kiriting: ')
#     n += 1
#     if mahsulotlar.lower() == 'enough':
#         break
#     narx = input(f'{mahsulotlar.capitalize()}ning narxini kiriting: ')
#     e_bozor[mahsulotlar] = float(narx)

# buyurtmalar = []

# print('\nNima buyurtirasiz: ')
# n = 1
# while True:
#     buyurtma = input(f'{n}-buyurtma: ')
#     n+=1
#     buyurtmalar.append(buyurtma)
#     if 'enough' in buyurtmalar:
#         break

# del buyurtmalar[-1]

# for byrt in e_bozor.keys():
#     if byrt in buyurtmalar:
#         print(f'{byrt.title()} ning narxi {e_bozor[byrt]}')
#     else:
#         print(f'{byrt} bizda yo\'q')



buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")