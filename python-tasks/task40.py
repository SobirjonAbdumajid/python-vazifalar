'''
Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
Foydalanuvchidan x va y sonlarini olib, ni konsolga chiqaruvchi funksiya yozing.
Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.

'''

# name = input('Your name: ')
# age = int(input('Your age:'))

# def tugulgan_yil_hisobla(name, age):
#     '''Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya.'''
#     print(f'Your name {name} and you were born in {2024 - age}.')

# tugulgan_yil_hisobla(name,age)




# def calculate_sqt_and_kub(num1):
#     '''Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya'''
#     print(f'Square of {num1} is {num1**2} and its cube is {num1**3}')

# calculate_sqt_and_kub(num1 = int(input('Enter number: ')))



# def find_OddOrEven_number(num1):
#     '''Sonni toq va juftlikga tekshiruvchi funksiya'''
#     if num1 % 2:
#         result = f'{num1} is odd'
#     else:
#         result = f'{num1} is even'
#     print(f'{result} number.')

# find_OddOrEven_number(int(input('Enter number: ')))

'''
def juftmi(son):
    """Kiritilgan son juft yoki toqligini konsolga chiqaruvchi funksiya"""
    if son%2:
        print(f"{son} toq son")
    else:
        print(f"{son} juft son")

juftmi(20)
juftmi(123)
'''



# def compare_numbers(num1, num2):
#     '''2 ta sonni taqqoslovchi funksiya'''
#     if num1 > num2:
#         max_num = num1
#     elif num2 > num1:
#         max_num = num2
#     else:
#         max_num = f'{num1} teng {num2} ga'
#     print(f'{max_num}')

# compare_numbers(int(input('Enter first number: ')),int(input('Enter second number: ')))


'''
def solishtir(x,y):
    """Ikki sonni solishtiruvchi funksiya"""
    if x>y:
        print(f"{x}>{y}")
    elif x<y:
        print(f"{y}>{x}")
    else:
        print(f"{x}={y}")

solishtir(10,20)
solishtir(-9,12)
solishtir(1223*5,5**4)
'''


# def level_up(num, degree):
#     '''Kiritilgan sonni kiritilgan songa oshirib beradigan funksiya (1-usul)'''
#     print(f'{num} ning {degree} darajasi {num**degree} ga teng.')

# level_up(float(input('Son kiriting: ')), float(input('Soznning darajasini kiriting: ')))

'''
def kv_kub(son):
    """Kiritilgan sonning kvadrati va kubini konsolga chiqaruvchi funksiya"""
    print(f"{son} ning kvadrati {son**2} ga, kubi {son**3} ga teng")

kv_kub(-4)
'''

# def level_up(num, degree = 2):
#     '''Kiritilgan sonni kiritilgan songa oshirib beradigan funksiya (2-usul)'''
#     print(f'{num} ning {degree} darajasi {num**degree} ga teng.')

# level_up(float(input('Son kiriting: ')))

'''
def daraja(x,y=2):
    print(f"{x} ning {y}-darajasi {x**y} ga teng")

daraja(5,2)
daraja(3,3)
daraja(94,4)
daraja(6)
'''



# def check_is_divide_num(mainnum):
#     '''Kiritilgan sonni 2 dan 11 gacha bo\'lgan sonlarga bo\'linishini tekshiruvchi funksiya.'''
#     for num in range(2,11):
#         if not mainnum % num:
#             print(f'{mainnum} {num} ga qoldiqsiz bo\'linadi.')
        
# check_is_divide_num(int(input('Son kiriting: ')))

'''
def bolinish_alomatlari(son):
    for n in range(2,11):
        if not son%n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")

bolinish_alomatlari(20)
'''