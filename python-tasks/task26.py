restoran_menu = {'kabob':60000,
                 'shashlik':10000,
                 'lag\'mon':30000,
                 'osh':25000,
                 'sho\'rva':23000,
                 'chuchvara':26000,
                 'qazi':35000,
                 'manti':5000,
                 'somsa':7000,
                 'honim':15000}
savat = []
print('3 ta ovqat buyurtiring!')
for num in range(3):
    savat.append(input(f'{num + 1} - ovqat: ').lower())

for svt in savat:    
    if svt in restoran_menu:
        print(f'{svt.capitalize()} {restoran_menu[svt]} so\'m')
    else:
        print(f'Kechirasiz, bizda {svt.capitalize()} yo\'q.')