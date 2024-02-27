def chek_chiqar(buyurtmalar_narx):
    '''Chek chiqarib beradigan funksiya'''
    for keys, values in buyurtmalar_narx.items():
        print(f'{int(values[1])} ta {keys.title()} {values[0]} bo\'ladi.')