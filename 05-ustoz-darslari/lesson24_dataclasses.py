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



from dataclasses import dataclass

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.len = (self.x + self.y) * 2
        
@dataclass
class Point2D:
    x: int
    y: int 
    
    def __post_init__(self):
        self.len = (self.x + self.y) * 2

pt1 = Point(1, 2)
print(pt1.len)
pt2 = Point2D(2, 3)
print(pt2.len)
pt3 = Point2D(2, 3)

print(pt2 == pt3)

