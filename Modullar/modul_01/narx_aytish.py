def narx_ayt(menu, buyurtmalar,mahsulot,soni):
    '''Narxini chiqarib beradigan funksiya'''
    result = menu[mahsulot] * soni
    print(f'{result} so\'m bo\'ldi,')
    buyurtmalar[mahsulot] = [result,soni]
    print('To\'htatish uchun STOP bosing: ')
