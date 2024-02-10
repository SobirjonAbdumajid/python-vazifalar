# mahsulotlar = ['somsa','kabob','tish cho\'tkasi','tish pastasi', 'noutbuk', 'sichqoncha','bakal','achki','qalam','ruchka']
# savat = []

# print('Savatga 5 ta mahsulot qo\'shing: ')
# for mahsulot in range(5):
#     savat.append(input(f'{mahsulot+1} - mahsulot: '))

# if savat:
#     for svt in savat:
#         if svt in mahsulotlar:
#             print(f'Bizda {svt} bor.') 
#         else:
#             print(f'Bizda {svt} yo\'q.')
# else:
#     print('Savat bo\'sh.')

mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = []

for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Do'konimizda {mahsulot} bor")
    else:
        print(f"Do'konimizda {mahsulot} yo'q")