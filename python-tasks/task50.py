# def multiply_numbers(*numbers):
#     '''It is function of mutiplier numbers'''
#     result = 1
#     for number in numbers:
#         result *= number
#     return result
# print(multiply_numbers(1,3,4))

def multiply(*sonlar):
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma

print(multiply(4,5,6))