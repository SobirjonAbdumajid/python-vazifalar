# # 1
# class Point:
#     def __init__(self, x):
#         self.x = x

#     # def __eq__(self, value):
#     #     return self.x == value.x and self.y == value.y
    
#     def __hash__(self):
#         return hash((self.x))

# pt1 = Point("dsadsadsa")

# print(hash(pt1))
# print(hash("qeqwewqewq"))

# print(None == None)


# 2
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __bool__(self):
        print("__bool__")
        return self.x == self.y
    
pt = Point(0, 1)

if pt:
    print('object pt give true')
else:
    print('false')
