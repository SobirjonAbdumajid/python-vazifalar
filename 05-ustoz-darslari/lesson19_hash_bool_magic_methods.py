class Point:
    def __init__(self, x):
        self.x = x

    # def __eq__(self, value):
    #     return self.x == value.x and self.y == value.y
    
    def __hash__(self):
        return hash((self.x))

pt1 = Point("dsadsadsa")

print(hash(pt1))
print(hash("qeqwewqewq"))