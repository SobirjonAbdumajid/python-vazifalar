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


# 3
class Point:
    def __init__(self, *args):
        self.__coords = args
    
    def __len__(self):
        return len(self.__coords)
pt = Point(1,2,3,4,5,6)
print(len(pt))
