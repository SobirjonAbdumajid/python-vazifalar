# # 1
# class Point:
#     @staticmethod
#     def draw():
#         print("draw works")

# class Logger:
#     @staticmethod
#     def save_log():
#         print("Logger works")

# class InsertDatabase:
#     @staticmethod
#     def insert():
#         print("insert works")

# class Notebook(Point, Logger, InsertDatabase):
#     pass

# n = Notebook()
# n.draw()
# n.save_log()
# n.insert()


# # 2
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     @staticmethod
#     def draw():
#         print("draw works")

# class Logger:
#     def __init__(self):
#         super.__init__()
#     @staticmethod
#     def save_log():
#         print("Logger works")


# class Notebook(Point, Logger):
#     pass

# n = Notebook(1,2)
# n.draw()
# n.save_log()
# print(Notebook.__mro__)


# 3
class Animal: # Animal
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def info(self):
        print(f"Info of {self.name}")


class Flyable: # Flyable
    def __init__(self, wing_span):
        self.wing_span = wing_span
    
    def fly(self):
        print(f"I can fly \nWing Span - {self.wing_span}")
        

class Swimmable: # Swimmable
    def __init__(self, swimming_speed):
        self.swimming_speed = swimming_speed

    def swim(self):
        print(f"Swimming speed - {self.swimming_speed}")



class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name, species, wing_span, swimming_speed):
        Animal.__init__(self, name, species)
        Flyable.__init__(self, wing_span)
        Swimmable.__init__(self, swimming_speed)
    
    def quack(self):
        print("Duck's method works")


class Pinguin(Animal, Swimmable):
    def __init__(self, name, species, swimming_speed):
        Animal.__init__(self, name, species)
        Swimmable.__init__(self, swimming_speed)
        
    def slide(self):
        print("Pinguin's method works")
        
        


d1 = Duck("Duck1's name", "duck", 1.5, 20)
d1.info()
d1.fly()
d1.swim()
d1.quack()

p1 = Pinguin("Pinguin1's name", "pinguin", 5)
p1.info()
p1.swim()
p1.slide()



