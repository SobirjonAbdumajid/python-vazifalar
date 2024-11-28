# # 1
# from abc import ABC, abstractmethod

# class Fruints(ABC):
#     @abstractmethod
#     def quantity(self):
#         raise NotImplementedError
    
# class Banana(Fruints):
#     def quantity(self):
#         print("This is quantity Banana")

# class Apple(Fruints):
#     def quantity(self):
#         print("This is quantity Apple")

# bn: Fruints = Banana()
# bn.quantity()

# from abc import ABC, abstractmethod

# class Figure(ABC):
#     def __init__(self, r=None, s1=None, s2=None):
#         self.radius = r
#         self.side1 = s1
#         self.side2 = s2
            
#     @abstractmethod
#     def area(self):
#         pass
    
#     @abstractmethod
#     def perimetr(self):
#         pass
    
#     @staticmethod
#     def info():
#         print("this is figure")
    
# class Rectangle(Figure):
#     pass
# class Circle(Figure):
#     pass
    
    
        



from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self, r=None, s1=None, s2=None):
        self.radius = r
        self.side1 = s1
        self.side2 = s2
            
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetr(self):
        pass
    
    @classmethod
    def info(cls):
        return cls.__name__

class Rectangle(Figure):
    def __init__(self, side1, side2):
        super().__init__(s1=side1, s2=side2)
    
    def area(self):
        return self.side1 * self.side2
    
    def perimetr(self):
        return 2 * (self.side1 + self.side2)

class Circle(Figure):
    def __init__(self, radius):
        super().__init__(r=radius)
        self.pi = 3.14

    def area(self):
        return self.pi * self.radius ** 2
    
    def perimetr(self):
        return 2 * self.pi * self.radius

rectangle = Rectangle(4, 5)
print(rectangle.area())
print(rectangle.perimetr())

print(rectangle.info())

circle = Circle(3)
print(circle.area())
print(circle.perimetr())

print(circle.info())
