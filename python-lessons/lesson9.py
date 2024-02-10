# talaba_0 = {'ism':'Sobirjon',
#             'familiya':'Abdumajidov',
#             'yosh':18,'t_yil':2005,
#             'fakultet':'IT',
#             'kurs':1}
# print(talaba_0)
# print(talaba_0.items())

# for kalit, qiymat in talaba_0.items():
#     print(f'Kalit {kalit}')
#     print(f'Qiymat {qiymat}')



# telefonlar = {'Sobirjon':'Galaxy A11','Dadam':'Galaxy A10','Ayam':'flash','Opam':'iPhone 7'}
# for k, q in telefonlar.items():
#     print(f'{k}ning telefoni {q}.')



# mahsulotlar = {'olma':10000,'anor':20000,'olcha':15000,'piyola':1000}
# # print(mahsulotlar.keys())
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot)

# for mahsulot in mahsulotlar:
#     print(mahsulot.title())



# mahsulotlar = {'olma':10000,'anor':20000,'olcha':15000,'piyola':1000}
# bozorlik = ['olma','telefon','batariya','olcha']
# for k, q in mahsulotlar.items():
#     if k in bozorlik:
#         print(f'{k.title()} {q} so\'m')



# mahsulotlar = {'olma':10000,'anor':20000,'olcha':15000,'piyola':1000}
# bozorlik = ['olma','telefon','batariya','olcha']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f'{mahsulot.title()} {mahsulotlar[mahsulot]} so\'m')

# for mahsulot in bozorlik:
#     if mahsulot not in mahsulotlar:
#         print(f'Iltimos, do\'koningizga {mahsulot}ni ham olib keling.')



# mahsulotlar = {'olma':10000,'anor':20000,'olcha':15000,'piyola':1000}
# print(sorted(mahsulotlar))
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())



# telefonlar = {'Sobirjon':'Galaxy A11','Dadam':'Galaxy A10','Ayam':'flash','Opam':'iPhone','kursdoshim1':'iPhone','kursdoshim2': 'iPhone'}
# print('Oilam quyidagi telefonlarni ishlatishadi:')
# for telefon in telefonlar.values():
#     print(telefon)



# telefonlar = {'Sobirjon':'Galaxy A11','Dadam':'Galaxy A10','Ayam':'flash','Opam':'iPhone','kursdoshim1':'iPhone','kursdoshim2': 'iPhone'}
# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi')
# for telefon in set(telefonlar.values()):
#     print(telefon)



# toys = {'bear','ball','car','lamp','ball','car'}
# print(type(toys))
# print(toys)