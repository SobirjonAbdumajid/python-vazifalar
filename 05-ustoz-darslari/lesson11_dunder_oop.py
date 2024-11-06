# # 1
# class Point:
#     def __init__(self):
#         print("Call __init__")
    
#     def __del__(self):
#         print("call __del__")
    
#     def aggregate_function(self):
#         print("Call abregate_function in Point")
    
# pt = Point()
# print(pt.aggregate_function())


# 2
class Rectangle:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        
    def find_area(self):
        return self.height * self.weight
    
    def find_perementr(self):
        return self.weight + self.weight + self.height + self.height

rectangle = Rectangle(12, 13)

print(rectangle.find_area())
print(rectangle.find_perementr())
