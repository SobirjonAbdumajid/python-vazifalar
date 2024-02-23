'''
Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini 
qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. 
Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)

Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan 
ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.
'''

def tell_a_person(name, surename, age, b_year, b_place, email = '', phone_number = 0):
    person = {
        'name':name,
        'surename':surename,
        'age':age,
        'b_year':b_year,
        'b_place':b_place,
        'email':email,
        'phone_number':phone_number
    }
    return person

people = []

while True:
    name = input('Your name: ')
    surename = input('Your surename: ')
    age = int(input('Your age: '))
    b_year = int(input('Brith year: '))
    b_place = input('Brith place: ')
    email = input('Your email: ')
    phone_number = input('Your phone number: ')

    people.append(tell_a_person(name,surename,age, b_year, b_place, email, phone_number))

    response = input('Do you want to add information about some person (yes / no): ')
    if response == 'no':
        break
print('Information about some people:')
for person in people:
    if person['email'] and person['phone_number']:
        email = person['email']
        phone_number = person['phone_number']
    else:
        email = 'Noma\'lum'
        phone_number = 'Noma\'lum'

    print(f'Users\' name {person['name']} and surname is {person['surename']}. User {person['age']} year old, phone number is {phone_number} also users email is {email}')
