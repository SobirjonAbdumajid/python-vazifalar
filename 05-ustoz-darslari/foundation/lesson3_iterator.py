'''
Iteratorlar & Topshiriqlar
'''

# # 1
# def main():
#     """
#     Bu funksiya iteratorni o'rganish uchun
#     """
#     L = ['Sobirjon', 'Abdumajidov']
#     m = iter(L)
#     print(next(m))
#     print(next(m))
#     # print(next(m)) # error
    

# if __name__ == '__main__':
#     main()
    


# # 2
# def main():
#     L = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]]
#     for i in L:
#         for j in i:
#             print(j)

# if __name__ == '__main__':
#     main()



# # 3
# def main():
#     """
#     Bu funksiya faktoryarni topadi
#     """
#     result = 1
#     faktoryar = int(input('son: '))
#     for i in range(1, faktoryar+1):
#         result *= i
#     print(result)

# if __name__ == '__main__':
#     main()



# # 4
# def main():
#     """
#     Bu funksiya x'sonigacha bo'lgan karra jadvalini chiqarib beradi
#     """
#     karra = int(input('karra: '))
#     for i in range(1, karra+1):
#         for j in range(1, 11):
#             print(i,' * ',j,f' = {i*j}')
#         print()

# if __name__ == '__main__':
#     main()



# # 5
# def main():
#     """
#     Bu funksiya berilgan sonning karra jadvalini chiqarib beradi
#     """
#     karra = int(input('karra: '))
#     for i in range(1, 11):
#         print(karra, ' * ', i, f' = {karra*i}')

# if __name__ == '__main__':
#     main()



# # 6
# student = [
#     ('Alina', [1, 3, 2]),
#     ('Ivan', [4, 1, 4]),
#     ('Charlie', [7, 3, 5]),
#     ('Islam', [4, 20, 2]),
# ]

# result = 0
# _dict = {}

# for i in student:
#     for j in i[1]:
#         result += j
#     _dict[f"{i[0]}"] = result
#     result = 0

# sorted_students = sorted(_dict.items(), key=lambda item: item[1], reverse=True)

# for student, score in sorted_students:
#     print(f"{student}: {score}")



# # 7
# def find_max2(n1,n2):
#     """
#     Bu funksiya eng katta raqamni topadi
#     """
#     return n1 if n1 > n2 else n2

# def find_max1(n1,n2,n3):
#     """
#     Bu funksiya eng katta raqamni topadi
#     """
#     return find_max2(n1 if n1 > n2 else n2, n3)
# print(find_max1(20,60,80))



# # 8
# class Test:
#     """
#     self'ning o'rniga istalgan boshqa so'z bilan ishlashining isboti
#     """
#     def __init__(ustoz, n1, n2):
#         ustoz.n1 = n1
#         ustoz.n2 = n2
#     def get_info(ustoz):
#         return ustoz.n1, ustoz.n2
        
# test = Test(1,3)
# print(test.get_info())



# # 9
# l = [
#     {
#     "name": "Laptop",
#     "price": 1500
#     },
#     {
#     "name": "Smartphone",
#     "price": 1000
#     },
#     {
#     "name": "Watch",
#     "price": 700
#     }
# ]

# def do(l, _max=False, _min=False):
#     """
#     Bu funksiya narxlarini argumentiga qarab chiqarib beradi
#     """
#     new_list = [unit['price'] for unit in l] # list comprehension
#     if _max and _min:
#         return max(new_list), min(new_list)
#     if _max:
#         return max(new_list)
#     return min(new_list)

# print(do(l, _min=True, _max=True))
