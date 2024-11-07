# 1
class Point:
    instance_count = 0
    def __new__(cls, x, y):
        cls.instance_count += 1
        return super().__new__(cls)
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
pt1 = Point(1, 2)
pt1 = Point(1, 2)
pt1 = Point(1, 2)


print(pt1.instance_count)