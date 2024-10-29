_str = 'Xamidovmalades'

_list = _str.split()
print(_str.split())
print(_str.count('a'))
print(type(_list))
print(_str.find('Xa'))
print(_str.isalpha())


# # # # # # name = "John"
# # # # # # age = 30
# # # # # # print("My name is {} and I am {} years old.".format('name', 'age'))

# # # # # ism = input("Ismingizni kiriting: ")
# # # # # # familiya = input("Familiyangizni kiriting: ")
# # # # # # nomer = input("Telefon raqamingizni kiriting: ")

# # # # # # print(f"Ism: {ism}, \nFamiliya: {familiya}, \nTelefon raqami: {nomer}")   

# # # # # print(f"ahmoq emas {ism}")
# # # # # # print("Familiya:", familiya)
# # # # # # print("Telefon raqami:", nomer)


# # # # # Bo'sh set yaratish
# # # # my_set = set()

# # # # # Elementlar bilan set yaratish
# # # # my_set = {1, 2, 3, 4, 4}
# # # # print(my_set)


# # # somsa = 'somsajon'
# # # # somsar = 54
# # # print(somsa[1])


# # # print(1 is '1')

# # res = "juft" if 41 % 2 == 0 else 'toq'
# # print(res)


# example = ["one", "two", 'three', 'four', 'five']

# while example:
#     try:
#         x = int(input("raqam: "))
#     except:
#         print('faqat int kiriting!')
#         break
    
#     for i in range(len(example)+1):
#         if x == i:
#             print(example[i-1])
            
    


list_of_number = ["one", "two", 'three', 'four', 'five']

# res_1 = []

# for i in list_of_number:
#     print(i)
#     res_1.append(i)
    
res_1 = [i for i in list_of_number]    

print(res_1)