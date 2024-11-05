# 1
# class Cats:
#     name = 'Pishak'
#     color = 'Qora'
#     age = 2
    
#     def set_name(self, name):
#         """
#         Example class function
#         """
#         self.name = name
#         print(f"This is {self.name}")
    
    
# cat1 = Cats() # instance
# cat2 = Cats()

# cat1.name = 'Alex'
# cat2.name = 'Mushuk'

# cat1.set_name('Oppoqoy')
# # print(cat1.name)
# # print(cat2.name)
# # print(cat1.name)
# # print(Cats().name)


# # 2
# class Cats:
#     name = "Pishak"
    
#     def get_pishak_name(self):
#         return 'Meow ' + self.name
    
# cat1 = Cats()
# print(cat1.get_pishak_name())
    


# # 3
# class Cats:
    
#     def set_name(self, name, color, age):
#         """
#         Example class function
#         """
        
#         self.name = name
#         self.color = color
#         self.age = age
    
#     def get_name(self):
#         return self.name, self.color, self.age
    

# cat1 = Cats() # instance
# cat2 = Cats()

# cat1.set_name('Oppoqoy', 'black', 1)

# setattr(cat2, 'name', 'Oppoqoy')
# setattr(cat2, 'color', 'white')
# setattr(cat2, 'age', 12)
# # print(getattr(cat2, 'name'))
# print(cat2.get_name())

# delattr(cat2, 'color')
# print(cat2.__dict__)


# 4
class Dogs:
    def set_attribute(self, name, age, breed, weight=False):
        self.name = name
        self.age = age
        self.weight = weight
        self.breed = breed
        
    def get_attribute(self):
        return self.name, self.age, self.breed, self.weight
    
    def bark(self):
        if self.weight:
            return 'This is ' + self.breed
    
dog1 = Dogs()
dog2 = Dogs()

dog1.set_attribute('John', 12, 'Apcharka', 321)
dog2.set_attribute('BOSHQA', 2, 'LAYCHA', 31)

print(dog1.get_attribute())
print(dog2.get_attribute())
