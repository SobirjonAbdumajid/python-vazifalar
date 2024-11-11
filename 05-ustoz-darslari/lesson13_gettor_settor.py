# # 1
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
        
#     @property
#     def get_name(self):
#         return self.__name
    
#     @get_name.setter
#     def set_name(self, name):
#         self.__name = name
#         return self.__name
    
#     @get_name.deleter
#     def del_name(self):
#         del self.__name
    
# person = Person("Habibullo", '1')
# person.set_name = 'Sobirjon'

# # del person.del_name
# # person.del_name()

# try:
#     print(person.get_name)
# except AttributeError:
#     print("The name has been deleted.")



# # 2
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self, name):
#         self.__name = name

#     @name.deleter
#     def name(self):
#         del self.__name

# person = Person("Habibullo", '1')

# person.name = 'Sobirjon'
# print(person.name)

# del person.name

# try:
#     print(person.name)
# except AttributeError:
#     print("The name has been deleted.")


#  sedan, hatchback, coupe, minivan, SUV
# class Car:
#     def __init__(self, nomi, color, price):
#         self.suvn
        

def find_type_and_price(car):
    _dict = {"Sedan":21000, "Hatchback":20000, "Coupe":22000, "Minivan":12000, "Suv":25000}
    price = _dict.get(car)
    # index_of = _list.index(car)
    
    return car, price
        

def main():
    _list = ["Sedan", "Hatchback", "Coupe", "Minivan", "Suv"]
    while True:
        print("""
        1. Sedan
        2. Hatchback
        3. Coupe
        4. Minivan
        5. Suv      
        """)
        try:
            carType = int(input("Tanlang: "))
            print(_list[carType + 1] + "ni tanladingiz")
        except:
            print('Son kiriting!')
            continue
        
        
        print(f"""
            1. {carType} Model A - $20000
            2. {carType} Sedan Model B - $22000
            3. {carType} Model C - $25000
              """)

        
main()
