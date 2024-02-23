# '''
# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
# '''

# def findMax_value(num1, num2, num3):
#     max_number = num1
#     if max_number < num2 and num2 > num3:
#         max_num = num2
#     elif max_number < num3:
#         max_num = num3
#     else:
#         max_num = num1
#     return max_num

# max_number = findMax_value(input('Enter first number: '),input('Enter second number: '),input('Enter third number: '))
# print(f'Max number is {max_number}')


def kattasi(x, y, z):
    max = x
    if y>=max:
        max = y
    if z>=max:
        max = z
    return max
katta = kattasi(200,50,70)
print(katta)