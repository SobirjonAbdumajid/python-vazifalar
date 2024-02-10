# age = int(input("Yoshingiz nechida?\n>>>"))
# if age <= 4 or age >= 60:
#     print('Siz muzeyga bepul kirishingiz mumkin.')
# elif age <= 18:
#     print('Sizga kirish 10000 so\'m bo\'ladi')
# elif age > 18:
#     print('Sizga muzeyga kirish 20000 so\'m bo\'ladi')



age = int(input("Yoshingiz nechida?\n>>>"))
if age <= 4 or age >= 60:
    narx = 0
elif age <= 18:
    narx = 10000
else:
    narx = 20000
print(f'Sizga muzeyga kirish {narx} so\'m')