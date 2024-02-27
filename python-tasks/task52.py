# kfs o'tirib yiysizmi ob ketasizmi. menu chiqarish(davomiy).ohirida chek funksiya bilan tuzilishi kerak
import sys
def menu_chiqar():
    '''MENU ni chop etadigan funksiya'''
    kfc = {'lavash':30000,
           'mini lavash':25000,
           'qahva':10000,
           'burger':25000,
           'hot dog':15000,
           'kfc':35000}

    option = input('O\'tirib yeysizmi olib ketasizmi: ')
    print('Nima buyurtma qilasiz:\nMENU:')
    for keys, values in kfc.items():
        print(f'{keys} - {values}',end=', ')  
    print()
    buyurtma_qabul_qil(kfc)



def buyurtma_qabul_qil(menu): # def buyurtma_qabul_qil(menu: int) -> bool:
    '''Buyurmat qabul qiladigan funksiya'''
    buyurtmalar = {}
    n = 1
    print('Nima buyurtirasiz.')
    while True:
        mahsulot = input(f'{n} - mahsulot: ').lower()
        if mahsulot == 'stop':
            while True:
                response = input('Chek kerakmi (ha/yo\'q):').lower()
                if response == 'ha':
                    chek_chiqar(buyurtmalar)
                    sys.exit()
                elif response == 'yo\'q':
                    print('Dastur tugadi!')
                    sys.exit()
                else:
                    print('Faqat ha/yo\'q deb javob berishingiz kerak.')
        else:
            if not mahsulot in menu:
                print('Bizda bunday mahsulot yo\'q.')
                continue
            else:
                n += 1
                soni = float(input('Nechta buyurtirasiz: '))
                narh_ayt(menu,buyurtmalar,mahsulot,soni)
               


def narh_ayt(menu, buyurtmalar,mahsulot,soni):
    '''Narxini chiqarib beradigan funksiya'''
    result = menu[mahsulot] * soni
    print(f'{result} so\'m bo\'ldi,')
    buyurtmalar[mahsulot] = [result,soni]
    print('To\'htatish uchun STOP bosing: ')



def chek_chiqar(buyurtmalar_narx):
    '''Chek chiqarib beradigan funksiya'''
    for keys, values in buyurtmalar_narx.items():
        print(f'{int(values[1])} ta {keys.title()} {values[0]} bo\'ladi.')

    

if __name__ == '__main__':
    menu_chiqar()