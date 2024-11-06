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


# # 2
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def find_area(self):
        return self.height * self.width
    
    def find_perimeter(self):
        return 2 * (self.height + self.width)

rectangle = Rectangle(height=12, width=13)

print(rectangle.find_area())


