# age = int(input('Yoshingiz nechida?: '))
# if age <= 4: narh = 4000
# elif age <= 12: narh = 6000
# elif age <= 18: narh = 8000
# else: narh = 10000
# print(f"Sizga kirish {narh} so'm")



# day = input('Bugun kun nima?\n>>>')
# if day.lower() == 'shanba' or day.lower() == 'yakshanba': print('Bugun dam olish kuni.')
# else: print("Bugun ish kuni.")



# day = input('bugun kun nima?\n>>>')
# degree = float(input('Havo harorati qanday?\n>>>'))
# if day.lower() == 'yakshanba' and degree >= 30: 
#     print("Ketting cho'milishga!")
# elif day.lower() == 'yakshanba' and degree < 30:
#     print("Bugun uyda dam olamiz")



# day = input('Bugungi kun: ')
# degree = int(input('Bugungi havo darajasi: '))
# if day.lower() == 'yakshanba' or day.lower() == 'shanba' and degree >= 30:
#     print("Cho'milishga kettik")
# elif day.lower() == 'yakshanba' or day.lower() == 'shanba' and degree < 30:
#     print('Bugun uyda dam olamiz.')



# xarid = 15000
# salat = False
# choy = True
# if salat and choy: xarid = xarid + 10000
# elif salat or choy: xarid = xarid + 5000
# print(f"Jami {xarid} so'm bo'ldi")



# narx = 15000
# choy = 0
# salat = 0
# non = 1
# kampot = 1
# assarti = 1
# if choy:    
#     print('Mijoz choy oldi')
#     narx = narx + 3000
# if salat:
#     print("Mijoz salat oldi.")
#     narx = narx + 5000
# if non:
#     print("Mijoz non oldi.")
#     narx = narx + 2800
# if kampot:
#     print('Mijoz kampot oldi.')
#     narx = narx + 5000
# if assarti:
#     print('Mijoz assarti oldi')
#     narx = narx + 15000
# print(f'Jami {narx} so\'m bo\'ldi')



# menu = ['somsa','osh','kabob','manti','shashlik']
# print('manti' in menu)



# menu = ['somsa','osh','kabob','manti','shashlik']
# buyurtma = input('Nima ovqat buyurtirasiz?\n>>> ')
# if buyurtma.lower() in menu:
#     print('Buyurtma qabul qilindi')
# else:
#     print(f'{buyurtma.title()} bizda mavjud emas.')




# menu = ['somsa','osh','kabob','manti','shashlik']
# buyurtma = input('Nima ovqat buyurtirasiz?\n>>> ')
# if buyurtma.lower() not in menu:
#     print(f'{buyurtma.title()} bizda mavjud emas.')
# else:
#     print('Buyurtma qabul qilindi')



# menu = ['somsa','osh','kabob','manti','shashlik','honim']
# buyurtmalar = ['somsa',"sho'rva",'manti','shashlik']
# for buyurtma in buyurtmalar:
#     if buyurtma.lower() in menu:
#         print(f"Bizda {buyurtma.capitalize()} bor.")
#     else:
#         print(f'Bizda {buyurtma.capitalize()} yo\'q')



# menu = ['somsa','osh','kabob','manti','shashlik','honim']
# buyurtmalar = ['somsa',"sho'rva",'manti','shashlik']

# if buyurtmalar:
#     for buyurtma in buyurtmalar:
#         if buyurtma.lower() in menu:
#             print(f'{buyurtma.capitalize()} bizda mavjud.')
#         else:
#             print(f'{buyurtma.capitalize()} bizda mavjud emas.')
# else:
#     print('Ro\'yxat bo\'sh.')