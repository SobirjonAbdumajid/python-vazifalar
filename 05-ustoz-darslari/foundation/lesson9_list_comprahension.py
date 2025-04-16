# # 1
# _list = [x for x in range(1,5)]
# print(_list)


# # 2
# _set = {y for y in range(1,5)}
# print(_set)


# # 3
# names = ["Alex", "Ivan", "Sergey"]
# _dict = {x:y for x, y in enumerate(names)}
# print(_dict)


# # 4
# _tuple = (y for y in range(1,5)) # bu generator bo'ladi
# print(_tuple)


# # 5
# def gen_list():
#     for i in range(5):
#         yield i
# l = gen_list()
# for x in l:
#     print(x ** 2)


# # 5
# while names:
#     for i, v in enumerate(names):
#         x = names.pop(i)
# print(names)


# # 6
# def gen_of(x):
#     for i in range(x):
#         yield i
# n = gen_of(10)
# for i in n:
#     print(i)


# # 7
# def find_prime_of(x=7):
#     _list = []
#     tub = 1
#     for i in range(2, x+1):
#         for j in range(1, i+1):
#             if i % j == 0:
#                 tub += 1
#                 _list.append(i)
            
#         if len(_list) == 2:
#             yield i
#         _list = []

# n = find_prime_of(12)
# for i in n:
#     print(i)


# # 8
# def find_divisin(x=7):
#     for i in range(1, x+1):
#         if (i % 4 == 0 and i % 6 != 0) or (i % 4 != 0 and i % 6 == 0):
#             yield i
            
# n = find_divisin(100)
# for i in n:
#     print(i)


# # 9
# def task():
#     for i in range(12):
#         if i % 4 == 0 and i % 6 == 0:
#             continue
#         elif i % 4 == 0 :
#             yield i
#         elif i % 6 == 0 :
#             yield i

# for x in task():
#     print(x)


# # 10
# veg = ["apple banana apple", "banana orange apple", "orange apple"]
# a = 0
# b = 0
# o = 0
# for i, v in enumerate(veg):
#     v = v.split()
#     print(v)
    
#     num_of_a = v.count('apple')
#     num_of_b = v.count('banana')
#     num_of_o = v.count('orange')
#     a += num_of_a
#     b += num_of_b
#     o += num_of_o
# # print(a)
# # print(b)
# # print(o)


# 11
veg = ["apple banana apple", "banana orange apple", "orange apple"]


def count_generator(veg: list[str]):
    counter_of = {}
    for i in veg:
        for j in i.split():
            counter_of[j] = counter_of.get(j, 0) + 1
    yield counter_of

for i in count_generator(veg):
    print(i)
    