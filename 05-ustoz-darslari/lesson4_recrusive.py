# # 1
# def find_factarial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * find_factarial(n-1)
    
# print(find_factarial(5))


# 2
def find_sum(n):
    birlik = n % 10
    onlik = (n//10)%10
    yuzlik = n//100
    
    return birlik + onlik + yuzlik

# print(find_sum(318))

# print((134//10)%10)


def find_sum_of(n):
    result = 0
    if len(n) == 1:
        result += n
    return n,find_sum(n//10)

print(find_sum(123))