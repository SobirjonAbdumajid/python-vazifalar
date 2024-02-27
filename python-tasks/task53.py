def recrusive(limit,n=1):
    n*=n
    
    if n == limit:
        return recrusive(limit,n=+1)
    else:
        return 3

limit = int(input('Son: '))    
print(recrusive(limit))

# songacha bo'lgan raqamlar yig'indisi

# limit = int(input('Son: '))
# result = 1
# for i in range(1,limit+1):
#     result+=i
#     if i == limit:
#         break
# print(result-1)

# limit = int(input('Son: '))
# result = 1
# for i in range(1,limit+1):
#     print(i)
#     result*=i
#     if i == limit:
#         break
# print(result)

