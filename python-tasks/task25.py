davlatlar = {'Aqsh':'Vashington',
             'O\'zbekiston':'Toshkent',
             'Tojikiston':'Dushanbe',
             'Turkiya':'Ankara'}

# print('Dunyo davlatlari:')
# for davlat in sorted(davlatlar):
#     print(davlat.capitalize())
# print('Davlatlar pytaxtlari:')
# for davlat in sorted(davlatlar.values()):
#     print(davlat.title())



# davlat = input("Qaysi davlatning poytaxtini bilishni istaysiz: ")
# print(davlatlar.get(davlat.capitalize(),'Bizda bunday ma\'lumot yo\'q'))



# davlat = input('Qaysi davlatning poytaxtini bilishni xohlaysiz: ').capitalize()
# capital = davlatlar.get(davlat)

# if capital == None:
#     print('Kechirasiz, bizda bunday ma\'lumot mavjud emas')
# else:
#     print(f'{davlat}ning poytaxti {capital} shahri.')



# davlat = input('Qaysi davlatni poytaxtini bilishni xohlaysiz: ').capitalize()
# if davlat in davlatlar:
#     print(f'{davlat} ning poytaxti {davlatlar[davlat]}')
# else:
#     print('Bunday ma\'lumot bizda mavjud emas.')



country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').capitalize()
capital = davlatlar.get(country)
if capital==None:
    print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
else:
    print(f"{country.upper()}ning poytaxti {capital.title()} shahri")