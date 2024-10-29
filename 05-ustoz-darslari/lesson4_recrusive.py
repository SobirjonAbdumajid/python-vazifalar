# # 1
# def find_factarial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * find_factarial(n-1)
    
# print(find_factarial(5))


# # 2
# def find_sum(n):
#     birlik = n % 10
#     onlik = (n//10)%10
#     yuzlik = n//100
    
#     return birlik + onlik + yuzlik

# print(find_sum(318))



# # 3
# def find_sum_of(n):
#     if n < 10:
#         return n
#     return n % 10 + find_sum_of(n//10)

# print(find_sum_of(123))


# 3
def find_sum_of(n):
    # Base case: if n is a single-digit number, return n itself
    if n < 10:
        return n
    else:
        # Recursive case: last digit + sum of remaining digits
        return n % 10 + find_sum_of(n // 10)

# Example usage
print(find_sum_of(123))
