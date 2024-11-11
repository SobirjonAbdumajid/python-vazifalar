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
        

class Cars:
    @staticmethod
    def get_cars():
        return {
            "sedan": {
                "1": "Toyota Camry",
                "2": "Honda Accord",
                "3": "Mazda6",
                "4": "BMW 3 Series",
                "5": "Mercedes-Benz C-Class"
            },
            "hatchback": {
                "1": "Volkswagen Golf",
                "2": "Ford Focus",
                "3": "Hyundai i30",
                "4": "Honda Civic Hatchback",
                "5": "Mazda3 Hatchback"
            },
            "coupe": {
                "1": "Ford Mustang",
                "2": "Chevrolet Camaro",
                "3": "BMW 4 Series",
                "4": "Audi A5",
                "5": "Mercedes-Benz C-Class Coupe"
            },
            "minivan": {
                "1": "Honda Odyssey",
                "2": "Toyota Sienna",
                "3": "Chrysler Pacifica",
                "4": "Kia Carnival",
                "5": "Dodge Grand Caravan"
            },
            "suv": {
                "1": "Toyota RAV4",
                "2": "Honda CR-V",
                "3": "Ford Explorer",
                "4": "Chevrolet Tahoe",
                "5": "Jeep Grand Cherokee"
            }
        }

        


def find_car_type(_list):
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
            print(_list[carType - 1] + "ni tanladingiz")
        except:
            print('Faqat son kiriting!\n1,2,3,4,5')
            continue
        else:
            return _list[carType - 1]
        
        

def find_car_model(cars, user_car):
    specific_car = cars[user_car.lower()]
    _list = []
    while True:
        for k, v in specific_car.items():
            print(f"{k}-{v}")
            _list.append()
        print(_list)
        print('Tanlang')
        user_model = input("")

def main():
    _list = ["Sedan", "Hatchback", "Coupe", "Minivan", "Suv"]
    user_car = find_car_type(_list)
    cars = Cars.get_cars()
    find_car_model(cars, user_car)
        
main()
