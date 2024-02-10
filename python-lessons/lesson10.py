car0 = {'model':'lacetti',
        'color':'white',
        'narx':13000}
car1 = {'model':'malibu',
        'color':'red',
        'narx':31000}
car2 = {'model':'nexia',
        'color':'qora',
        'narx':10000}

car = car0
print(f'{car['model'].title()} \
      {car['color'].title()}\
      {car['narx']}')
car = car1
print(f'{car['model'].title()} \
      {car['color'].title()}\
      {car['narx']}')
car = car2
print(f'{car['model'].title()} \
      {car['color'].title()}\
      {car['narx']}')



cars = [car0,car1,car2]
for car in cars:
    print(f'{car['model'].title()}, '
          f'{car['color'].title()} rang, '
          f'{car['narx']}$')
print(cars[0])
print(cars[0]['model'])


# malibus = []
# for n in range(10):
#     new_car = {'model':'malibu',
#             'color':None,
#             'year':2024,
#             'price':None,
#             'km':0,
#             'korobka':'avto'}
#     malibus.append(new_car)

# for malibu in malibus[:3]:
#     malibu['color'] = 'qizil'

# for malibu in malibus[3:6]:
#     malibu['color'] = 'qora'

# for malibu in malibus[6:]:
#     malibu['color'] = 'qora'
#     malibu['korobka'] = 'mexanika'

# for malibu in malibus:
#     print(malibu)

# for malibu in malibus:
#     if malibu['korobka'] == 'avto':
#         malibu['price'] = 40000
#     else:
#         malibu['price'] = 35000

# for malibu in malibus:
#     print(malibu)



# dasturchilar = {
#     'sobirjon':['c++','c#','python','dart','html','css'],
#     'sardor':['html','css','js'],
#     'abduqahhor':['python','js'],
#     'umidjon':['c++','c#']
#     }

# for ism,tillar in dasturchilar.items():
#     print(f'{ism.title()} quyidagi dasturlash tillarini biladi: ')
#     for til in tillar:
#         print(til.upper()+' ' ,end='')



# hamkasblar = {
#     'sobirjon':{
#         'familiya':'Abdumajidov',
#         't_yil':2005,
#         'ma\'lumot':'o\'rta mahsus',
#         'tillar':['python','c#']
#     },
    
#     'abduqahhor':{
#         'familiya':'abdusattorov',
#         't_yil':2006,
#         'ma\'lumot':'oliy',
#         'tillar':['html','dart']
#     },

#     'umidjon':{
#         'familiya':'jumaniyazov',
#         't_yil':2005,
#         'ma\'lumot':'mahsus',
#         'tillar':['html','css','c++']
#     }
# }

# for ism, malumot in hamkasblar.items():
#     print(f'\n{ism.title()} {malumot['t_yil']} - yilda tug\'ilgan.\nMa\'lumoti: {malumot['ma\'lumot']}. \nQuyidagi dasturlash tillarini biladi:')
#     for info in malumot['tillar']:
#         print(info.upper())