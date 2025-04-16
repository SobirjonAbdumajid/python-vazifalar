# # 1
# def funk_decorator(func):
#     def wrapper():
#         print("-----------------------")
#         func()
#         print("-----------------------")
#     return wrapper

# @funk_decorator
# def just_print():
#     print("Sobirjon")
    
# just_print()


# 2
import time

def cache_decorator(func):
    cache = {}  # Natijalarni saqlab turadigan bo‘sh joy (kesh)

    def wrapper(x):  # Funksiyani o‘rab turuvchi
        if x in cache:  # Agar natija oldin saqlangan bo‘lsa
            print("Keshdan olindi:", x)
            return cache[x]  # Natijani keshdan oladi
        else:
            result = func(x)  # Funksiyani chaqiradi va natijani hisoblaydi
            cache[x] = result  # Natijani keshga saqlaydi
            return result

    return wrapper

@cache_decorator
def uzun_hisoblash(x):
    time.sleep(2)  # 2 soniya kutish (og‘ir hisoblanish imitatsiyasi)
    return x * x

print(uzun_hisoblash(5))  # Hisoblash 2 soniya kutadi
print(uzun_hisoblash(5))  # Natija keshdan olinadi, kutmaymiz
print(uzun_hisoblash(10)) # Yangi qiymat, yana 2 soniya kutadi
print(uzun_hisoblash(5))  # Keshda bor, natija darhol chiqadi

