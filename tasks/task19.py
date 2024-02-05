# mahsulotlar = ['somsa','kabob','tish cho\'tkasi','tish pastasi', 'noutbuk', 'sichqoncha','bakal','achki','qalam','ruchka']
# bor_mahsulotlar = []
# mavjud_emas = []
# savat = []
# print('Mahsulotlarni kiriting!')
# for n in range(5):
#     savat.append(input(f'{n+1} - mahsulot: '))
# for svt in savat:
#     if svt.lower() in mahsulotlar:
#         bor_mahsulotlar.append(svt)
#     else:
#         mavjud_emas.append(svt)
# if len(mavjud_emas) == 0:
#     print('Siz so\'ragan hamma mahsulotlar bizda mavjud.')
# else:
#     print('Quyidagi mahsulotlar do\'konimizda yo\'q')
#     for m_e in mavjud_emas:
#         print(m_e)

mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = []

for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
  print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
  for mahsulot in mavjud_emas:
    print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")