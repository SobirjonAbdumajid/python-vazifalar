import chek_chiqarish,sys,narx_aytish
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
                    chek_chiqarish.chek_chiqar(buyurtmalar)
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
                narx_aytish.narx_ayt(menu,buyurtmalar,mahsulot,soni)
               