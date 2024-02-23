# def change_upper(texts):
#     results = []
#     while texts:
#         upper_letter = texts.pop().title()
#         results.append(upper_letter)
#     return results

# words = ['sobirjon','sardor','abbos','abduqahhor']
# final_result = change_upper(words[:])
# print(final_result)
# print(words)



# def katta_harf(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()   

# ismlar = ['ali', 'vali', 'hasan', 'husan']
# katta_harf(ismlar)
# print(ismlar)



def katta_harf(matnlar):
    matnlar = matnlar[:]
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].title()
    return matnlar

ismlar = ['ali', 'vali', 'hasan', 'husan']
yangi_ismlar = katta_harf(ismlar)
print(ismlar)
print(yangi_ismlar)