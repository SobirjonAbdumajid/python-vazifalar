# import math

# uzunlik = lambda pi, r: 2 * pi * r
# print(uzunlik(math.pi,2))

# kvadrat = lambda n1, n2: n1 ** n2
# print(kvadrat(2,3))



# def daraja(number):
#     return lambda x : x ** number
# kvadrat = daraja(2)
# kub = daraja(3)
# print(f'3 ning kvadrati {kvadrat(3)} ga kubi {kub(3)} ga teng.')

# from math import sqrt

# numbers = list(range(11))
# result1 = list(map(sqrt,numbers))
# print(result1)

# --------------------------------------------------------------

# def kvadrat(x):
#     '''Berilgan sonning kvadratini qaytaruvchi funksiya'''
#     return x*x
# result2 = list(map(kvadrat,numbers))
# print(result2)

# --------------------------------------------------------------

# result2 = list(map(lambda x : x*x,numbers))
# print(result2)

# --------------------------------------------------------------

# collectionOfNumbers1 = [3,5,6]
# collectionOfNumbers2 = [1,24,6]
# result2 = list(map(lambda x, y:x+y,collectionOfNumbers1,collectionOfNumbers2))
# print(result2)



# import random as r

# numbers = r.sample(range(100),10)
# print(numbers)

# --------------------------------------------------------------

# def iseven(n):
#     '''Juft bo\'lsa true toq bo\'lsa false qaytaruvchi funksiya'''
#     return n % 2 == 0

# even_numbers = list(filter(iseven,numbers))
# print(even_numbers)

# # print(iseven(4))
# # print(iseven(3))

# --------------------------------------------------------------

# even_number = list(filter(lambda x:x%2==0,numbers))
# print(even_number)



# fruits = ['olma','anor','olcha','anjir','kiwi','banan']
# # letter = 'o'
# # result = list(filter(lambda fruit : fruit.startswith(letter),fruits))
# # print(result)

# fruits2 = list(filter(lambda fruit : len(fruit)<5,fruits))
# print(fruits2)
