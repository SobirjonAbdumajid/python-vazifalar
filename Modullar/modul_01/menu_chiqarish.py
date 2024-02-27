import buyurtma_qabul_qilish
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
    buyurtma_qabul_qilish.buyurtma_qabul_qil(kfc)
    # from buyurtma_qabul_qilish import buyurtma_qabul_qil(kfc)
