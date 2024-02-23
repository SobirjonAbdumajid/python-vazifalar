'''
To'plamdan uchramas elementlarni o'chirish.
To'plam berilgan. Ushbu to'plamdan faqat bir marta uchraydigan elementlarni o'chiring.

Yaniy: [1, 2, 3, "a", 3, 2, 1] => [1, 2, 3, 3, 2, 1]

'''

# elementlar = [1, 2, 3, 'a', 3, 2, 1]
# for element in elementlar:
#     if type(element) == str:
#         elementlar.remove(element)
#     else:
#         print(element)

# print(sorted(elementlar))



# elementlar = [1, 2, 3, 'a', 3, 2, 1]
# for element in elementlar:
#     if element and element in elementlar:
#         # elementlar.remove(element)
#         print(element)
# print(elementlar)

# my_list = [1, 2, 3, 'a', 3, 2, 1]
# unique_list = list(set(my_list))
# print(unique_list)  # Natija: [1, 2, 3, 4, 5]

            # my_list = [1, 2, 3, 'adsfds', 6,7,8,9, 3, 2, 1]
            # unique_list = [x for x in my_list if my_list.count(x) == 1]
            # print(unique_list)  # Natija: [1, 3, 5]
            # print(my_list)

            # for u_l in unique_list:  
            #     my_list.remove(u_l)

            # print(my_list)


# my_list = [1, 2, 3, 'a', 3, 2, 1]
# unique_elements = []
# seen_elements = set()

# for x in my_list:
#     if x not in seen_elements:
#         seen_elements.add(x)
#         unique_elements.append(x)

# print(unique_elements)  # Natija: [1, 3, 5]

my_list = [1, 2, 3, 'adsfds', 6, 7, 8, 9, 3, 2, 1]
unique_list = [x for x in my_list if my_list.count(x) == 1]
print(unique_list)  # Natija: [1, 3, 'adsfds', 6, 7, 8, 9]

for u_l in unique_list:
    while u_l in my_list:
        my_list.remove(u_l)

print(my_list)  # Natija: [2, 3, 1, 2, 1]