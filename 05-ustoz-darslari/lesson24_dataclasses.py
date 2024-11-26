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



# # 3
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#         self.total_value = self.price * self.quantity

# @dataclass
# class Products:
#     name: str
#     price: float
#     quantity: int
    
#     def __post_init__(self):
#         self.total_value = self.price * self.quantity



# p1 = Product("Laptop", 123.3, 11)
# print(p1.total_value)


# p1 = Products(123.3, 11)
# print(p1, p1.total_value)


# # 3
# from dataclasses import dataclass, field

# @dataclass
# class Example:
#     a: int
#     b: int
#     c: list = field(default_factory=list)
    
# ex = Example(1,2,[3,4,5])
# ex.c.append(6)
# ex2 = Example(1,2)
# print(ex.c, ex2.c)


# # 4
# from dataclasses import dataclass, field

# class Example:
#     a: int
#     b: int = field(default=2, compare=True)
#     c: int = field()
    
    
# 5
from dataclasses import dataclass, field

# class User:
#     def __init__(self, name: str):
#         self.name = name
#         self.friends = []
#         self.posts = []
        
#     def add_friend(self, friend):
#         self.friends.append(friend)
    
#     def add_post(self, post):
#         self.posts.append(post)
    
#     def list_posts(self):
#         return self.posts

@dataclass
class User:
    name: str
    friends: list = field(default_factory=list)
    posts: list = field(default_factory=list)
    
    def add_friend(self, friend):
        self.friends.append(friend)
    
    def add_post(self, post):
        self.posts.append(post)
    
    def list_posts(self):
        return self.posts
        

u1 = User("Sobirjon", [], [])
u1.add_friend("Xabibullo")
u1.add_friend("Sardorbek")
u1.add_post("Xabibullo is Sobirjon's best friend ever")
u1.add_post("Sardorbek is Sobirjon's best friend ever")
print(u1.list_posts()) 


