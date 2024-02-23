# son = 1

# while son <= 5:
#     print(son, end=' ')
#     son += 1

# print('dastur tugadi')



# print('Kiritilgan sonning kvadratini qaytaruvchi dastur.')
# savol = 'Son kiriting: '
# savol += 'dasturni tugatish uchun \'exit\' deb yozing: '
# qiymat = ''

# while qiymat.lower() != 'exit':
#     qiymat = input(savol)
#     if qiymat.lower() != 'exit':
#         print(float(qiymat)**2)
# print('Dastur tugadi')



# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input('Son kiriting: ')
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print('Dastur tugadi.')



# qiymat = ''
# ishora = True

# while ishora:
#     qiymat = input('Raqam kiriting: ')
#     if qiymat.lower() == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)

# print('Dastur tugadi.')



# qiymat = ''

# while True:
#     qiymat = input('Son kiriting: ')
#     if qiymat.lower() == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)
# print('Dastur tugadi.')



# sonlar = list(range(1,11))

# for son in sonlar:
#     if son == 5:
#         break
#     print(son, 'ning kvadrati',son**2,'ga teng.')
# print('Dastur tugadi.')



# sonlar = list(range(1,11))

# for son in sonlar:
#     if son == 5:
#         continue
#     print(son,'ning kivadrati',son**2,'ga teng.')
# print('Dastur tugadi.')



son = 0

while son <= 10:
    son+=1
    if son%2 != 0:
        continue
    else:
        print(son)
print('Dastur tugadi.')