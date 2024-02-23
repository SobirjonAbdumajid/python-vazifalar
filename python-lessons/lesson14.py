# def tell_full_name(name, surename):
#     '''Telling full name of person'''
#     full_name = f'You are {name} {surename}'
#     return full_name

# fullname = tell_full_name('Sobirjon','Abdumajidov')
# print(fullname)



# def tell_full_name(name, surename, otasining_ismi = ''):
#     '''Telling full name of person'''
#     if otasining_ismi:
#         fullName = (f'{name} {surename} {otasining_ismi}')
#     else:
#         fullName = (f'{name} {surename}')
#     return fullName.title()
# fullName2 = tell_full_name('sobirjon','abdumajidov')
# fullName1 = tell_full_name('sobirjon','abdumajidov','Akmal o\'g\'li')

# print(f'Darsga kelmagan o\'quvchilar: {fullName1} va {fullName1}')



# def give_info_about_avtos(kompaniya, model, color, box, year, price = None):
#     '''Avtomabillar haqida ma\'lumotlar beruvchi funksiya'''
#     avto = {
#         'kompaniya':kompaniya,
#         'model':model,
#         'color':color,
#         'box':box,
#         'year':year,
#         'price':price
#     }
#     return avto

# avto1 = give_info_about_avtos('gm','malibu','black','avto',2024)
# avto2 = give_info_about_avtos('tesla','tesla car','white','avto',2023,45000)

# avtolar = [avto1,avto2]

# for avto in avtolar:
#     if avto['price']:
#         price = avto['price']
#     else:
#         price = 'noma\'lum'

#     print(f'{avto['color']} {avto['model']}, Narhi: {price}')



# def show_differenceOfNumbers(min, max):
#     '''Ikki sonning orasidagi sonlarni chiqarib beruvchi funksiya.'''
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min += 1
#     return sonlar
# print(show_differenceOfNumbers(1,11))
# print(show_differenceOfNumbers(20,30))

# def show_differenceOfNumbers(min, max, step = 0):
#     '''Ikki sonning orasidagi sonlarni chiqarib beruvchi funksiya.'''
#     sonlar = []
#     while min < max:
#         if step:
#             sonlar.append(min)
#             min += 2
#         else:
#             sonlar.append(min)
#             min += 1
#     return sonlar
# print(show_differenceOfNumbers(1,11))
# print(show_differenceOfNumbers(0,10,2))



def give_info_about_avtos(kompaniya, model, color, box, year, price = None):
    '''Avtomabillar haqida ma\'lumotlar beruvchi funksiya'''
    avto = {
        'kompaniya':kompaniya,
        'model':model,
        'color':color,
        'box':box,
        'year':year,
        'price':price
    }
    return avto

cars = []
while True:
    kompaniya = input('Ishlab chiqaruvchi: ')
    model = input('Modeli ')
    color = input('Rangi: ')
    box = input('Karobka: ')
    year = input('Ishlab chiqarilgan yili: ')
    price = input('Narhi: ')
    
    cars.append(give_info_about_avtos(kompaniya,model,color,box,year,price))

    response = input('Wonna add car again (yes/no): ')
    if response == 'no':
        break

print('\nCars in car park:')
for car in cars:
    if car['price']:
        price = car['price']
    else:
        price = 'Noma\'lum'
    print(f'{car['color']} {car['model']}, its price: {price}')
