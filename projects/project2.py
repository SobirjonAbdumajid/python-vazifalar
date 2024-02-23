'''Mijoz talablari:
Omborxona tizimini shakllantirish:
1. mahsulotlar qo`shish
2. mahsulot ni update qilish
3. mahsulot tanlanganda ushbu mahsulotdan qancha qolganligini olish
4.Qolmagan mahsulotlar ro’yxatini chiqarib berish
 
Siz ombor  tizimini boshqaradigan kompyuter dasturini loyihalash va ishlab chiqish vazifasini oldingiz. 
'''

mahsulotlar = []
print('Omborga mahsulotlar qo\'shing (stop tuhtatish): ')
n = 1
while True:
    mahsulotlar.append(input(f'{n} - mahsulot: '))
    n+=1
    if 'stop' in mahsulotlar:
        mahsulotlar.remove('stop')
        break
print('Ishlatilgan mahsulotlarni kiriting (stop tuhtatish): ')

ishlatilgan_mahsulot = []

while True:
    ishlatilgan_mahsulot.append(input('Qaysi mahsulotlar ishlatildi: '))
    if 'stop' in ishlatilgan_mahsulot:
        ishlatilgan_mahsulot.remove('stop')
        break


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