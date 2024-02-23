# # end = int(input("Son: "))
# end = 2
# start = 1

# num1 = 1
# num2 = 2


# while True:
#     print(num1)
#     print(num2)
#     print(num1+num2)
#     print(num1+num2-num1)
#     break
#     # if start < end:
        
#         # # print(start)
#         # fibanachi = start
#         # # start == 1
#         # start += 1
#         # fibanachi += start

# n = 10

# fibanachi = [0]
# a = 0
# b = 1

# while len(fibanachi) < n:
#     fibanachi.append(b)
#     a, b = b, a + b

# print(fibanachi)


num1 = 0
num2 = 1
fibanachi = 0
given_number = int(input('Enter number: '))

while given_number > fibanachi:
    print(fibanachi)
    fibanachi = num1 + num2
    num1 = num2
    num2 = fibanachi



# def find_fibanachi_number(limit,fibanachi = 0,n1 = 0,n2 = 1):
#     while limit > fibanachi:
#         print(fibanachi)
#         fibanachi = n1 + n2
#         n1 = n2
#         n2 = fibanachi
        
# print(find_fibanachi_number(int(input('Son kiriting: '))))

# a = 0
# b = 1
# given_number = int(input("Raqam kiriting: "))
# fibi = 0
# while given_number > fibi:
#     print(fibi)
#     fibi = a + b
#     a = b
#     b = fibi





# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         print(x)
#         if x == 0 or x == 1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x - 1] + sonlar[x - 2])
#     return sonlar


# print(fibonacci(10))
