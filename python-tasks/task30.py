# buxoriy = {
#     'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#     't_yil':810,
#     't_joy':'buxoro',
#     'umr':60
# }

# qodiriy = {
#     'ism':'abdulla qodiriy',
#     't_yil':1894,
#     't_joy':'toshkent',
#     'umr':44
# }

# vohidov = {
#     'ism':'erkin vohidov',
#     't_yil':1936,
#     't_joy':'farg\'ona',
#     'umr':80
# }

# navoiy = {
#     'ism':'alisher navoiy',
#     't_yil':1441,
#     't_joy':'xirot',
#     'umr':60
# }

# shahslar = [buxoriy,qodiriy,vohidov,navoiy]

# # for shahs in shahslar:
# #     print(f'{shahs['ism'].title()} {shahs['t_yil']} - yilda {shahs['t_joy'].capitalize()}da tavvallud topganlar. {shahs['umr']} yil umr ko\'rganlar.')



# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro'
#            }

# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent'
#            }

# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona"
#            }

# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot"
#            }

# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     tyil = shaxs['tyil']
#     vyil = shaxs['vyil']
#     tjoy = shaxs['tjoy']
#     print(f"{ism} {tyil}-yilda {tjoy}da tavallud topgan. "
#           f"{vyil-tyil} yil umr ko'rgan.")



# buxoriy.update({'asarlar':['Al-jome\' as-sahih','Al-adab Al-mufrad','At-tarix al-kabir','At-tarix as-sag\'r']})
# qodiriy.update({'asarlar':['o\'tkan kunlar','mehrobdan chayon','obid ketmon']})
# vohidov.update({'asarlar':['tong nafasi','qo\'shiqlarim sizga','o\'zbegim','qiziquvchan matmusa']})
# navoiy.update({'asarlar':['xamsa','lison ut-tayr','mahbub al-qulub']})

# print(shahslar)

# for shahs in shahslar:
#     print(f'\n{shahs["ism"].title()}ning mashhur asarlari:')
#     for shahs_asar in shahs['asarlar']:
#         print(f'{shahs_asar.title()}')


buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
           'tyil':810,
           'vyil':870,
           'tjoy':'Buxoro',
           'asarlar':["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]
           }

qodiriy = {'ism':'Abdulla Qodiriy',
           'tyil':1894,
           'vyil':1938,
           'tjoy':'Toshkent',
           'asarlar':["O'tkan kunlar","Mehrobdan Chayon",'Obid ketmon']
           }

vohidov = {'ism':'Erkin Vohidov',
           'tyil':1936,
           'vyil':2016,
           'tjoy':"Farg'ona",
           'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
           }

navoiy = {'ism':'Alisher Navoiy',
           'tyil':1441,
           'vyil':1501,
           'tjoy':"Xirot",
           'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
           }

shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

for shaxs in shaxslar:
    ism = shaxs['ism']
    asarlar = shaxs['asarlar']
    print(f"\n{ism} ning mashxur asarlari: ")
    for asar in asarlar:
        print(asar)