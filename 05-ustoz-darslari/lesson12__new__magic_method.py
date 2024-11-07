# # 1
# class Point:
#     instance_count = 0
#     def __new__(cls, x, y):
#         cls.instance_count += 1
#         return super().__new__(cls)
    
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
# pt1 = Point(1, 2)
# pt1 = Point(1, 2)
# pt1 = Point(1, 2)

# print(pt1.instance_count)


# 2
class Circle:
    __pi = 3.14
    
    def __init__(self, radius):
        self.radius = radius
        
    def length_circle(self):
        return 2 * self.__pi * self.radius
circle = Circle(5)
print(circle.length_circle())
circle.__pi = 4
print(circle.length_circle())