# oilam_sevimli_kinoVaseriallari = {
#     'onam':['t-34','qo\'rg\'on sirlari'],
#     'dadam':['facebookdagi kinolar','youtobedagi kinolar'],
#     'opam':['koreya kinolar','koreya seriyallari']
# }

# for k, v in oilam_sevimli_kinoVaseriallari.items():
#     print(f'\n{k.title()}ning sevimli kinolari: ')
#     for kino in v:
#         print(kino.title())



kinolar = {
    'ali':['Terminator','Rambo','Titanic'],
    'vali':['Tenet','Inception','Interstellar'],
    'hasan':['Abdullajon','Bomba','Shaytanat'],
    'husan':['Mahallada duv-duv gap','John Wick']
    }

for ism, kinolar in kinolar.items():
    print(f"\n{ism.title()}ning sevimli kinolari:")
    for kino in kinolar:
        print(kino)