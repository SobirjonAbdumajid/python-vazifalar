# # 1
# A = type('Point', (), {'x':0, 'y':0})

# a = A()
# # a.x = 3
# print(a.x)


# # 2
# class Women:
#     women_id = "This is women id"
#     women_name = "This is women name"
#     women_age = "This is women age"

#     def __init__(self, login, pasw):
#         self.login = login
#         self.pasw = pasw
#         self.meta = self.Meta(login + "@" + pasw)
    
#     class Meta:
#         def __init__(self, access):
#             self._access = access

# w = Women('root', '1234')
# print(w.__dict__)
# print(w.meta.__dict__)



# # 3
# def create_meta_class(clas, inh, attrs):
#     attrs.update({"MAX_COORD":100, "MIN_COURDS":0})
#     return type(clas, inh, attrs)

# class Meta(type):
#     def __new__(cls, name, base, attrs):
#         attrs.update({"MAX_COORD":100, "MIN_COURDS":-100})
#         return type.__new__(cls, name, base, attrs)
    
#     def __init__(cls, name, base, attrs):
#         super().__init__(name, base, attrs)
#         cls.MAX_COORD = 100
#         cls.MIN_COORD = 0

# class Point(metaclass=Meta):
#     @staticmethod
#     def get_coord():
#         return 'Ok'
    
# pt = Point()
# print(pt.MAX_COORD)
        

# 5
def voice(self): # 2nd way
    print(f"{self.name}'s voice")
    
A = type('Animal', (), {
    'name':'', 
    'typee':'', 
    'age':0, 
    # 'voice': lambda self: print(f"{self.name}'s voice") # 1st way
    'voice': voice # 2nd way
})

a = A()

a.name = "Sher"
a.typee = "Yirtqich"
a.age = 3

print(a.name)
print(a.typee)
print(a.age)
a.voice()



# # 6
# class A:
#     def __init__(self, name, typee, age):
#         self.name = name
#         self.typee = typee
#         self.age = age
        
#     def voice(self):
#         print(f"{self.name}'s voice")

# a = A("Sher", "Yirtqich", 3)


# print(a.name)
# print(a.typee)
# print(a.age)
# a.voice()
