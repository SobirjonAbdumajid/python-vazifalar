# while True:
#     age = input('Yoshingizni kiriting: ')
#     if age.lower() == 'exit' or age.lower() == 'quit':
#         break
#     elif int(age) <= 7:
#         print('2000 so\'m')
#     elif int(age) <= 18:
#         print('3000 so\'m')
#     elif int(age) < 65:
#         print('10000 so\'m')
#     else:
#         print('Siz uchun bepul.')

# print('Dastur tugadi.')



# age = ''

# while age != 'quit' or age != 'exit':
#     age = input('Yoshingiz nechida: ')
#     if age.lower() == 'quit' or age.lower() == 'exit':
#         break
#     elif int(age) <= 7:
#         print('Siz uchun muzeyga kirish 2000 so\'m.')
#     elif int(age) <= 18:
#         print('Siz uchun muzeyga kirish 3000 so\'m.')
#     elif int(age) < 65:
#         print('Siz uchun muzeyga kirish 10000 so\'m.')
#     else:
#         print('Siz uchun muzeyga kirish bepul.')

# print('Dastur ishi yakunlandi.')



# logic = True
# while logic:
#     age = input('Yoshingizni kiriting: ')
#     if age.lower() == 'quit' or age.lower() == 'exit':
#         logic = False
#     elif int(age) <= 7:
#         print('Siz uchun muzeyga kirish 2000 so\'m')
#     elif int(age) <= 18:
#         print('Siz uchun muzayga kirish 3000 so\'m.')
#     elif int(age) < 65:
#         print('Siz uchun muzeyga kirish 10000 so\'m.')
#     else:
#         print('Siz uchun muzeyga kirish bepul.')
# print('Dashtur ishi yakunlandi.')



savol = "Yoshingizni kiriting: "

while True:
    qiymat = input(savol)
    if qiymat == 'exit' or qiymat == 'quit':
        break
    yosh = int(qiymat)
    
    if yosh<7:
        narh = 2000
    elif 7<=yosh<18:
        narh = 3000
    elif 18<=yosh<65:
        narh = 10000
    else: narh = 0
    
    if narh==0:
        print("Sizga chipta bepul")
    else:
        print(f"Chipta {narh} so'm")