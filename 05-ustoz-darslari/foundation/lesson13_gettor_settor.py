# # # 1
# # class Person:
# #     def __init__(self, name, age):
# #         self.__name = name
# #         self.__age = age
        
# #     @property
# #     def get_name(self):
# #         return self.__name
    
# #     @get_name.setter
# #     def set_name(self, name):
# #         self.__name = name
# #         return self.__name
    
# #     @get_name.deleter
# #     def del_name(self):
# #         del self.__name
    
# # person = Person("Habibullo", '1')
# # person.set_name = 'Sobirjon'

# # # del person.del_name
# # # person.del_name()

# # try:
# #     print(person.get_name)
# # except AttributeError:
# #     print("The name has been deleted.")



# # # 2
# # class Person:
# #     def __init__(self, name, age):
# #         self.__name = name
# #         self.__age = age

# #     @property
# #     def name(self):
# #         return self.__name

# #     @name.setter
# #     def name(self, name):
# #         self.__name = name

# #     @name.deleter
# #     def name(self):
# #         del self.__name

# # person = Person("Habibullo", '1')

# # person.name = 'Sobirjon'
# # print(person.name)

# # del person.name

# # try:
# #     print(person.name)
# # except AttributeError:
# #     print("The name has been deleted.")


# #  sedan, hatchback, coupe, minivan, SUV
# # class Car:
# #     def __init__(self, nomi, color, price):
# #         self.suvn
        
        
        

# class Cars:
#     @staticmethod
#     def get_cars():
#         return {
#         1: {"sedan": {
#                 "1": {"name": "Toyota Camry", "price": "$25,000"},
#                 "2": {"name": "Honda Accord", "price": "$26,500"},
#                 "3": {"name": "Mazda6", "price": "$27,000"},
#                 "4": {"name": "BMW 3 Series", "price": "$41,500"},
#                 "5": {"name": "Mercedes-Benz C-Class", "price": "$43,000"}
#             }},
#         2: {"hatchback": {
#                 "1": {"name": "Volkswagen Golf", "price": "$23,500"},
#                 "2": {"name": "Ford Focus", "price": "$22,000"},
#                 "3": {"name": "Hyundai i30", "price": "$24,000"},
#                 "4": {"name": "Honda Civic Hatchback", "price": "$25,500"},
#                 "5": {"name": "Mazda3 Hatchback", "price": "$26,000"}
#             }},
#         3: {"coupe": {
#                 "1": {"name": "Ford Mustang", "price": "$55,000"},
#                 "2": {"name": "Chevrolet Camaro", "price": "$50,000"},
#                 "3": {"name": "BMW 4 Series", "price": "$52,000"},
#                 "4": {"name": "Audi A5", "price": "$53,500"},
#                 "5": {"name": "Mercedes-Benz C-Class Coupe", "price": "$54,000"}
#             }},
#         4: {"minivan": {
#                 "1": {"name": "Honda Odyssey", "price": "$33,500"},
#                 "2": {"name": "Toyota Sienna", "price": "$34,500"},
#                 "3": {"name": "Chrysler Pacifica", "price": "$36,000"},
#                 "4": {"name": "Kia Carnival", "price": "$32,500"},
#                 "5": {"name": "Dodge Grand Caravan", "price": "$31,500"}
#             }},
#         5: {"suv": {
#                 "1": {"name": "Toyota RAV4", "price": "$29,500"},
#                 "2": {"name": "Honda CR-V", "price": "$28,500"},
#                 "3": {"name": "Ford Explorer", "price": "$36,500"},
#                 "4": {"name": "Chevrolet Tahoe", "price": "$49,000"},
#                 "5": {"name": "Jeep Grand Cherokee", "price": "$47,500"}
#             }}
#     }

        


# def find_car_type(cars):
#     while True:
#         print("""
#         1. Sedan
#         2. Hatchback
#         3. Coupe
#         4. Minivan
#         5. Suv      
#         """)
#         try:
#             _input = int(input("Tanlang: "))
#             all_info_car = cars.get(_input)
#             car_category = list(cars[_input].keys())[0]
#             print(f"{car_category.capitalize()} turini tanladingiz.\n")        
#         except:
#             print('Faqat son kiriting!\n1,2,3,4,5')
#             continue
#         else:
#             return all_info_car
        
# def return_prices(specific_car):
#     info = specific_car.keys()
#     car_category = list(specific_car.keys())[0]
    
#     for k, v in specific_car[car_category].items():
#         print(k+'.', v)
    
#     name = "Tanlang!\n"

# # def find_car_model(cars, user_car):
# #     specific_car = cars[user_car.lower()]
# #     _list = []
# #     while True:
# #         for k, v in specific_car.items():
# #             print(f"{k}-{v}")
# #             _list.append()
# #         print(_list)
# #         print('Tanlang')
# #         user_model = input("")

# def main():
#     _list = ["Sedan", "Hatchback", "Coupe", "Minivan", "Suv"]
#     cars = Cars.get_cars()
    
#     somsa1 = find_car_type(cars)
#     somsa2 = return_prices(somsa1)
        
# main()



class Cars:
    @staticmethod
    def get_cars():
        return {
            1: {"sedan": {
                    "1": {"name": "Toyota Camry", "price": "$25,000"},
                    "2": {"name": "Honda Accord", "price": "$26,500"},
                    "3": {"name": "Mazda6", "price": "$27,000"},
                    "4": {"name": "BMW 3 Series", "price": "$41,500"},
                    "5": {"name": "Mercedes-Benz C-Class", "price": "$43,000"}
                }},
            2: {"hatchback": {
                    "1": {"name": "Volkswagen Golf", "price": "$23,500"},
                    "2": {"name": "Ford Focus", "price": "$22,000"},
                    "3": {"name": "Hyundai i30", "price": "$24,000"},
                    "4": {"name": "Honda Civic Hatchback", "price": "$25,500"},
                    "5": {"name": "Mazda3 Hatchback", "price": "$26,000"}
                }},
            3: {"coupe": {
                    "1": {"name": "Ford Mustang", "price": "$55,000"},
                    "2": {"name": "Chevrolet Camaro", "price": "$50,000"},
                    "3": {"name": "BMW 4 Series", "price": "$52,000"},
                    "4": {"name": "Audi A5", "price": "$53,500"},
                    "5": {"name": "Mercedes-Benz C-Class Coupe", "price": "$54,000"}
                }},
            4: {"minivan": {
                    "1": {"name": "Honda Odyssey", "price": "$33,500"},
                    "2": {"name": "Toyota Sienna", "price": "$34,500"},
                    "3": {"name": "Chrysler Pacifica", "price": "$36,000"},
                    "4": {"name": "Kia Carnival", "price": "$32,500"},
                    "5": {"name": "Dodge Grand Caravan", "price": "$31,500"}
                }},
            5: {"suv": {
                    "1": {"name": "Toyota RAV4", "price": "$29,500"},
                    "2": {"name": "Honda CR-V", "price": "$28,500"},
                    "3": {"name": "Ford Explorer", "price": "$36,500"},
                    "4": {"name": "Chevrolet Tahoe", "price": "$49,000"},
                    "5": {"name": "Jeep Grand Cherokee", "price": "$47,500"}
                }}
        }

def find_car_type(cars):
    while True:
        print("""
        1. Sedan
        2. Hatchback
        3. Coupe
        4. Minivan
        5. Suv      
        """)
        try:
            _input = int(input("Tanlang: "))
            all_info_car = cars[_input]  # Raises KeyError if the key doesn't exist
            car_category = list(all_info_car.keys())[0]
            print(f"{car_category.capitalize()} turini tanladingiz.\n")
        except (ValueError, KeyError):
            print('Faqat son kiriting!\n1,2,3,4,5')
            continue
        else:
            return all_info_car




def return_prices(specific_car):
    car_category = list(specific_car.keys())[0]
    print(f"{car_category.capitalize()} modellari va narxlari:\n")
    
    for car_id, car_info in specific_car[car_category].items():
        print(f"{car_id}. {car_info['name']} - {car_info['price']}")

    while True:
        try:
            _input = int(input("Mashina raqamini tanlang (1-5): "))
            
            if str(_input) in specific_car[car_category]:
                selected_car = specific_car[car_category][str(_input)]
                print(f"\nSiz tanlagan mashina: {selected_car['name']} - Narxi: {selected_car['price']}")
                
                # Convert the price to a float by removing the dollar sign and commas
                base_price = float(selected_car['price'].replace('$', '').replace(',', ''))
                return base_price  # Return the numeric base price for further calculations
            else:
                print("Faqat 1 dan 5 gacha bo'lgan raqamlarni kiriting.")
        except ValueError:
            print("Faqat son kiriting!\n1,2,3,4,5")




def return_colors_price(base_price):
    print("""
    Available colors:
    1. Oq (0% extra money)
    2. Qora (3% extra money)
    3. Malla (2% extra money)
    """)

    color_price_adjustments = {
        "1": 0.0,
        "2": 0.03,
        "3": 0.02
    }

    while True:
        color_choice = input("Select a color by entering its number (1-3): ")
        if color_choice in color_price_adjustments:
            color_name = ["Oq", "Qora", "Malla"][int(color_choice) - 1]
            extra_percentage = color_price_adjustments[color_choice]
            final_price = base_price * (1 + extra_percentage)
            print(f"\nYou selected: {color_name}")
            print(f"Base Price: ${base_price:.2f}")
            print(f"Final Price (after color adjustment): ${final_price:.2f}\n")
            return final_price
        else:
            print("Please enter a valid number (1-3).")


def main():
    cars = Cars.get_cars()
    selected_car_type = find_car_type(cars)
    price = return_prices(selected_car_type)
    final_price = return_colors_price(price)
    print(f"Total Final Price: ${final_price:.2f}")
    
    while True:
        print('Tasdiqlaysizmi?')
        _input = input('>>>')
        if _input.lower() == 'ha':
            print("Sotib oldingiz\nSavdo tugadi")
            break
        elif _input.lower() == "yo'q":
            print("Savdo bekor qilindi")
        else:
            print("Iltimos faqat ha/yo'q kiriting")
            continue
        
            
if __name__ == "__main__":
    main()
