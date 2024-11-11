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
    def get_sedan():
        sedan_cars = {
        "1": "Toyota Camry",
        "2": "Honda Accord",
        "3": "Mazda6",
        "4": "BMW 3 Series",
        "5": "Mercedes-Benz C-Class"
        }

    hatchback_cars = {
        "1": "Volkswagen Golf",
        "2": "Ford Focus",
        "3": "Hyundai i30",
        "4": "Honda Civic Hatchback",
        "5": "Mazda3 Hatchback"
    }

    coupe_cars = {
        "1": "Ford Mustang",
        "2": "Chevrolet Camaro",
        "3": "BMW 4 Series",
        "4": "Audi A5",
        "5": "Mercedes-Benz C-Class Coupe"
    }

    minivan_cars = {
        "1": "Honda Odyssey",
        "2": "Toyota Sienna",
        "3": "Chrysler Pacifica",
        "4": "Kia Carnival",
        "5": "Dodge Grand Caravan"
    }

    suv_cars = {
        "1": "Toyota RAV4",
        "2": "Honda CR-V",
        "3": "Ford Explorer",
        "4": "Chevrolet Tahoe",
        "5": "Jeep Grand Cherokee"
    }




def find_type_and_price(car):
    _dict = {"Sedan":21000, "Hatchback":20000, "Coupe":22000, "Minivan":12000, "Suv":25000}
    price = _dict.get(car)
    # index_of = _list.index(car)
    
    return car, price
        


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
        
        

def find_car_model(_dict, carType):
    
    while True:
        print(f"""
            1. {carType} Model A - ${_dict.get(carType)}
            2. {carType} Sedan Model B - ${_dict.get(carType)}
            3. {carType} Model C - ${_dict.get(carType)}
              """)

def main():
    
    
    
    
    _list = ["Sedan", "Hatchback", "Coupe", "Minivan", "Suv"]
    carType = find_car_type(_list)
    find_car_model(_dict, carType)
        
main()
