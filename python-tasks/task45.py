'''Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing 
(tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)'''

# def show_prime_numbers(start, end):
#     '''Tub sonlar ro'yxatini qaytaruvchi funksiya'''
#     for limit in range(start,end):
#         if limit % 2 != 0 and limit % 3 != 0 and limit % 5 != 0:
#             print(limit)
# show_prime_numbers(0,20)


# def show_prime_numbers(start, end):
#     '''Tub sonlar ro'yxatini qaytaruvchi funksiya'''
#     for limit1 in range(start, end):
#         if limit1 > 1:
#             for limit2 in range(2, end):
#                 if limit1 % limit2 == 0:
#                     print(limit1)
# show_prime_numbers(1,20)

# def find_prime_numbers(start, end):
#     prime_numbers = []
#     for num in range(start, end + 1):
#         if num > 1:
#             for i in range(2, int(num ** 0.5) + 1):
#                 if num % i == 0:
#                     break
#             else:
#                 prime_numbers.append(num)
#     return prime_numbers

# primes = find_prime_numbers(1, 100)
# print(primes)



def tub_sonlar_top(min, max):
    tub_sonlar = []
    for n in range(min, max + 1):
        tub = True
        if n == 1:
            tub = False
        elif n == 2:
            tub = True
        else:
            for x in range(2, n):
                if n % x == 0:
                    tub = False
        if tub:
            tub_sonlar.append(n)
                
    return tub_sonlar
tub_number = tub_sonlar_top(1,20)
print(tub_number)