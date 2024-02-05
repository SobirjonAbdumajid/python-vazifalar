# number = int(input('Istalgan butun son kiriting: '))
# for n in range(2,11):
#     if number % n == 0:
#         print(f'{number} soni {n} ga qoldiqsiz bo\'lidadi')

son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")