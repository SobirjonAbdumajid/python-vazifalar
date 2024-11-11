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


# # 2
# class Circle:
#     __pi = 3.14
    
#     def __init__(self, radius):
#         self.radius = radius
        
#     def length_circle(self):
#         return 2 * self.__pi * self.radius
# circle = Circle(5)
# print(circle.length_circle())
# circle.__pi = 4
# print(circle.length_circle())


# 3
class Rectangle:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width
        
    def find_area(self):
        return self.__height * self.__width
    
    def find_perimetr(self):
        return 2 * (self.__height + self.__width)
    
    def is_square(self):
        return self.__height == self.__width
    
    def resize(self, n_height, n_width):
        self.__height = n_height
        self.__width = n_width
        return self.__height, self.__width

rectangle = Rectangle(2, 12)
# rectangle.height = 1972933746
print(rectangle.resize(20, 30))
print(rectangle.find_area())


# # 4
# class FileHandler:
#     def __init__(self, filename):
#         self.file = open(filename, 'w')
#         print(f"{filename} ochildi.")

#     def __del__(self):
#         self.file.close()
#         print(f"{self.file.name} yopildi va xotira tozalandi.")

# # Fayl bilan ishlash
# file_handler = FileHandler('test.txt')

# # Fayl endi kerak bo'lmasa
# del file_handler  # Bu yerda fayl avtomatik ravishda yopiladi va xotira tozalanadi
