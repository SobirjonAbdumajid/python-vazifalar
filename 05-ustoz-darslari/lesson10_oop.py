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


class Cats:
    name = "Pishak"
    
    def get_pishak_name(self):
        return 'Meow ' + self.name
    
cat1 = Cats()
print(cat1.get_pishak_name())
    

