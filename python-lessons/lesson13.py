# def salom_ber(ism):
#     '''Foydalanuvchining ismi bilan salom beradigon funksiya'''
#     print(f'Assalomu alaykum {ism.title()}')

# salom_ber('sobirjon')
# salom_ber('sardor')

# print(salom_ber.__doc__)
# print(print.__doc__)



# def toliq_yosh_hisobla(ism,tugulgan_yil):
#     '''Foydalanuvchining yoshini hisoblovchi dastur.'''
#     print(f'Foydalanuvchining ismi {ism}'
#           f'va u {2024 - tugulgan_yil} yoshda')

# toliq_yosh_hisobla(tugulgan_yil = 2005, ism = 'Sobirjon')



def yosh_hisobla(tugulgan_yil, joriy_yil = 2024):
    '''Yosh hisoblaydigan funksiya'''
    print(f'Siz {joriy_yil - tugulgan_yil} yoshdasiz')
yosh_hisobla(2005)