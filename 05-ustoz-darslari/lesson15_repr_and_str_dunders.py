# # 1
# class Cat:
#     def __init__(self, name):
#         self.name = name
        
#     def __repr__(self):
#         return f'{self.__class__}: {self.name}'
    
#     def __str__(self):
#         return self.name
    
# ct = Cat("Alex")
# ct
# print(str(ct))
# print(ct)


# # 2
# def example(*args):
#     print(type(args))

# example([1, 2, 3])


# # 3
# class Point:
#     def __init__(self, *args):
#         self.__coords = args
    
#     def __len__(self):
#         return len(self.__coords)
# pt = Point(1,2,3,4,5,6)
# print(len(pt))


# # 4
# def square(x):
#     return x * x

# numbers = [1, 2, 3, 4, 5, -3]

# squared_numbers = map(square, numbers)

# print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]
# print(list(map(abs, numbers)))


# # 5
# class Point:
#     def __init__(self, *args):
#         self.__coords = args
    
#     def __len__(self):
#         return len(self.__coords)
    
#     def __abs__(self):
#         return list(map(abs, self.__coords))
    
# pt = Point(1,2,3,4,5,-6)
# print(len(pt))

# print(abs(pt))


# # 6
# class Number:
#     def __init__(self, *args):
#         self.num = args
    
#     def __repr__(self):
#         return f'{self.__class__}: {self.num}'
    
#     def __str__(self):
#         return str(self.num)
    
#     def __len__(self):
#         _list = list(self.num[:])
#         if _list[0] < 0:
#             _list[0] = _list[0] * -1
#         return len(str(_list[0]))
    
#     def __abs__(self):
#         return list(map(abs, self.num))
    
# number = Number(182)
# print('len', len(number))
# print(number)
# print('abs', abs(number))


# 7
class Number:
    def __init__(self, num):
        self.num = num
    
    def __repr__(self):
        return f'{self.__class__}: {self.num}'
    
    def __str__(self):
        return str(self.num)
    
    def __len__(self):
        return len(str(abs(self.num)))
    
    def __abs__(self):
        return abs(self.num)
    
number = Number(-2182)
print('len', len(number))
print('str', number)
print('repr', repr(number))
print('abs', abs(number))
