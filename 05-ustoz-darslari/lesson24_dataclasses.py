from dataclasses import dataclass
# # 1
# from dataclasses import dataclass

# class Point:
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y
        
#     @dataclass
#     class Point2D:
#         x: int
#         y: int

# pt1 = Point(1, 2)
# pt2 = Point(2, 3)
# pt3 = Point(2, 3)

# print(pt2 == pt3)



# # 2
# from dataclasses import dataclass

# class Point:
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y
#         self.len = (self.x + self.y) * 2
        
# @dataclass
# class Point2D:
#     x: int
#     y: int 
    
#     def __post_init__(self):
#         self.len = (self.x + self.y) * 2

# pt1 = Point(1, 2)
# print(pt1.len)
# pt2 = Point2D(2, 3)
# print(pt2.len)
# pt3 = Point2D(2, 3)

# print(pt2 == pt3)


# 3
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total_value = self.price * self.quantity

@dataclass
class Products:
    price: float
    quantity: int
    
    def __post_init__(self):
        self.total_value = self.price * self.quantity



p1 = Product("Laptop", 123.3, 11)
print(p1.total_value)


p1 = Products(123.3, 11)
print(p1, p1.total_value)
