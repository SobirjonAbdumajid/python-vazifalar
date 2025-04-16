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


# # 4
# class Geom:
#     name = "Geom"
    
#     def draw(self):
#         print('Draw geom')
        
# class Line(Geom):
#     name = "Line"
    
#     def draw(self):
#         print('Draw Line')

# class Circle(Geom):
#     name = "Circle"
    
#     def draw(self):
#         print('Draw Circle')
     
# class Rectangle:
#     def draw(self):
#         print('Draw Rectangle')
      
# print(issubclass(object, Circle))



# # 5
# class Product:
#     def __init__(self, name, product_id, quantity, price):
#         self.name = name
#         self.product_id = product_id
#         self.quantity = quantity
#         self.price = price
        
#     def __repr__(self):
#         return f'{self.__class__.__name__}: {self.name}'
    
#     def __str__(self):
#         return str(self.name)
        

# class Warehouse(Product):
#     def __init__(self, name, product_id, quantity, price, **kwargs = ):
#         super().__init__(name, product_id, quantity, price)
#         self.kwargs = kwargs
    
#     def add_product(self, adr, product_id):
#         self.kwargs[adr] = product_id
        
#     def remove_product(self, adr):
#         del self.kwargs[adr]
        
#     def get_product(self):
#         return self.kwargs
    
# warehouse = Warehouse('Laptop', 1, 4, 123)
                


# 6
class Product:
    def __init__(self, name, product_id, quantity, price):
        self.name = name
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
        
    def __repr__(self):
        return f'{self.__class__.__name__}: {self.name}'
    
    def __str__(self):
        return str(self.name)
        

class Warehouse(Product):
    def __init__(self, name, product_id, quantity, price, **kwargs):
        super().__init__(name, product_id, quantity, price)
        self.kwargs = kwargs
        
    def add_product(self, adr, product_id):
        self.kwargs[adr] = product_id
        
    def remove_product(self, adr):
        if adr in self.kwargs:
            del self.kwargs[adr]
        else:
            print(f"'{adr}' - not found.")

    def get_product(self):
        return self.kwargs
    

warehouse = Warehouse('Laptop', 1, 4, 123)

warehouse.add_product('Shelf_1', 101)
warehouse.add_product('Shelf_2', 102)

print(warehouse.get_product())

warehouse.remove_product('Shelf_1')
print(warehouse.get_product())
