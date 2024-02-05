foydalanuvchilar = ['Sobirjon','Sardor','Umidjon','Ilhomjon','Abduqahhor']
foydalanuvchi = input('Yangi login tanlang: ')
if foydalanuvchi.capitalize() in foydalanuvchilar:
    print(f'{foydalanuvchi.capitalize()} Logini band, yangi login tanlang!')
else:
    foydalanuvchilar.append(foydalanuvchi.capitalize())
    print(f'{foydalanuvchi.capitalize()} Xush kelibsiz!')