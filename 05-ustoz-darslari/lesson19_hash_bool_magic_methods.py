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


# # 2
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def __bool__(self):
#         print("__bool__")
#         return self.x == self.y
    
# pt = Point(0, 1)

# if pt:
#     print('object pt give true')
# else:
#     print('false')


# # 3
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)

#     def __getitem__(self, item):
#         return self.marks[item]
    
#     def __setitem__(self, key, value):
#         self.marks[key] = value
        
#     def __delitem__(self, key):
#         del self.marks[key]
        
# s1 = Student('Sergey', [5,5,3,2,5])
# print(s1[2])
# s1[2] = 4
# print(s1[2])
# del s1[2]
# print(s1[2])

class Geom:
    name = "Geom"
    
    def draw(self):
        print('Draw geom')
        
    

class Line(Geom):
    name = "Line"
    
    def draw(self):
        print('Draw Line')
        
    

class Circle(Geom):
    name = "Circle"
    
    def draw(self):
        print('Draw Circle')
     
        
class Rectangle:
    def draw(self):
        print('Draw Rectangle')
      

print(issubclass(Geom, Circle))

# g = Geom()
        
    
