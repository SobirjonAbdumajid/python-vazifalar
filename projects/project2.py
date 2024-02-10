'''Mijoz talablari:
Omborxona tizimini shakllantirish:
1. mahsulotlar qo`shish
2. mahsulot ni update qilish
3. mahsulot tanlanganda ushbu mahsulotdan qancha qolganligini olish
4.Qolmagan mahsulotlar ro’yxatini chiqarib berish
 
Siz ombor  tizimini boshqaradigan kompyuter dasturini loyihalash va ishlab chiqish vazifasini oldingiz. 
'''

mahsulotlar = []
n_of_products = int(input('Nechta mahsulot qo\'shmoqchisiz: '))
for n in range(n_of_products):
    mahsulotlar.append(input(f'{n + 1} - mahsulot: '))

n_of_ishlatilgan_mahsulotlar = int(input('Nechta mahsulot ishlatildi: '))

ishlatilgan_mahsulot = []

for i_m in range(n_of_ishlatilgan_mahsulotlar):
    ishlatilgan_mahsulot.append(input('Qaysi mahsulotlar ishlatildi: '))

for i_m in ishlatilgan_mahsulot:
    if i_m in mahsulotlar:
        mahsulotlar.remove(i_m)

respons = input('Qolgan mahsulotlarni ko\'rmoqchimisiz (ha/yo\'q): ')

if respons == 'ha':
    print('Qolgan mahsulotlar: ')
    for mahsulot in mahsulotlar:
        print(mahsulot)
elif respons == 'yo\'q':
    print('Tugagan va kerak bo\'lgan mahsulotlar:')
    for i_m in ishlatilgan_mahsulot:
        print(i_m)