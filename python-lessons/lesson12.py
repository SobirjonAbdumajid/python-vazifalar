# print('Do\'stlaringizni ro\'yxatini tuzamiz.')
# ismlar = []
# n = 1 
# while True:
#     savol = f'{n} - do\'stingizni ismini kiriting: '
#     ismlar.append(input(savol))
#     takrorlash = input('Yana ism qo\'shasizmi (ha/yo\'q): ')
#     n+=1
#     if takrorlash.lower() != 'ha':
#         break

# print('\nDo\'stlaringizni ro\'yxati: ')
# for ism in ismlar:
#     print(ism.title())



# dostlar = {}
# logic = True

# while logic:
#     ism = input('Do\'stingizni ismini kiriting: ')
#     yosh = input('Do\'stingizni yoshini kiriting: ')
     
#     # dostlar[input('Do\'stingizni ismini kiriting: ')] = input('Do\'stingizni yoshini kiriting: ')
#     dostlar[ism] = int(yosh)
#     javob = input('Yana do\'stlaringiz haqida ma\'lumotlar kiritmoqchimisiz (ha/yo\'q): ')
#     if javob.lower() == 'yo\'q':
#         logic = False

# for ism, yosh in dostlar.items():
#     print(f'{ism.title()} {yosh} yoshda')



# cars = ['lacetti','nexia','cobalt','nexia','toyota','audi','nexia']
# print(cars)
# car = 'lacetti'
# while car in cars:
#     cars.remove(car)

# print(cars)



talabalar = ['sardor','sobirjon','abduqahhor','umidjon','ilhomjon']
baholangan_talabalar = {}

while talabalar:
    talaba = talabalar.pop()
    baho = input(f'{talaba.title()}ning baxosino kiriting: ')
    print(f'{talaba.title()} baxolandi.')
    baholangan_talabalar[talaba] = int(baho)

print(talabalar)
print(baholangan_talabalar)
    