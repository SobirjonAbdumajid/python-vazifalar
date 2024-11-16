# # class Cars:
# #     @staticmethod
# #     def get_cars():
# #         return {
# #             1: {"sedan": {
# #                     "1": {"name": "Toyota Camry", "price": "$25,000"},
# #                     "2": {"name": "Honda Accord", "price": "$26,500"},
# #                     "3": {"name": "Mazda6", "price": "$27,000"},
# #                     "4": {"name": "BMW 3 Series", "price": "$41,500"},
# #                     "5": {"name": "Mercedes-Benz C-Class", "price": "$43,000"}
# #                 }},
# #             2: {"hatchback": {
# #                     "1": {"name": "Volkswagen Golf", "price": "$23,500"},
# #                     "2": {"name": "Ford Focus", "price": "$22,000"},
# #                     "3": {"name": "Hyundai i30", "price": "$24,000"},
# #                     "4": {"name": "Honda Civic Hatchback", "price": "$25,500"},
# #                     "5": {"name": "Mazda3 Hatchback", "price": "$26,000"}
# #                 }},
# #             3: {"coupe": {
# #                     "1": {"name": "Ford Mustang", "price": "$55,000"},
# #                     "2": {"name": "Chevrolet Camaro", "price": "$50,000"},
# #                     "3": {"name": "BMW 4 Series", "price": "$52,000"},
# #                     "4": {"name": "Audi A5", "price": "$53,500"},
# #                     "5": {"name": "Mercedes-Benz C-Class Coupe", "price": "$54,000"}
# #                 }},
# #             4: {"minivan": {
# #                     "1": {"name": "Honda Odyssey", "price": "$33,500"},
# #                     "2": {"name": "Toyota Sienna", "price": "$34,500"},
# #                     "3": {"name": "Chrysler Pacifica", "price": "$36,000"},
# #                     "4": {"name": "Kia Carnival", "price": "$32,500"},
# #                     "5": {"name": "Dodge Grand Caravan", "price": "$31,500"}
# #                 }},
# #             5: {"suv": {
# #                     "1": {"name": "Toyota RAV4", "price": "$29,500"},
# #                     "2": {"name": "Honda CR-V", "price": "$28,500"},
# #                     "3": {"name": "Ford Explorer", "price": "$36,500"},
# #                     "4": {"name": "Chevrolet Tahoe", "price": "$49,000"},
# #                     "5": {"name": "Jeep Grand Cherokee", "price": "$47,500"}
# #                 }}
# #         }

# # def find_car_type(cars):
# #     while True:
# #         print("""
# #         1. Sedan
# #         2. Hatchback
# #         3. Coupe
# #         4. Minivan
# #         5. Suv      
# #         """)
# #         try:
# #             _input = int(input("Tanlang: "))
# #             all_info_car = cars[_input]
# #             car_category = list(all_info_car.keys())[0]
# #             print(f"{car_category.capitalize()} turini tanladingiz.\n")
# #         except (ValueError, KeyError):
# #             print('Faqat son kiriting!\n1,2,3,4,5')
# #             continue
# #         else:
# #             return all_info_car




# # def return_prices(specific_car):
# #     car_category = list(specific_car.keys())[0]
# #     print(f"{car_category.capitalize()} modellari va narxlari:\n")
    
# #     for car_id, car_info in specific_car[car_category].items():
# #         print(f"{car_id}. {car_info['name']} - {car_info['price']}")

# #     while True:
# #         try:
# #             _input = int(input("Mashina raqamini tanlang (1-5): "))
            
# #             if str(_input) in specific_car[car_category]:
# #                 selected_car = specific_car[car_category][str(_input)]
# #                 print(f"\nSiz tanlagan mashina: {selected_car['name']} - Narxi: {selected_car['price']}")
                
# #                 base_price = float(selected_car['price'].replace('$', '').replace(',', ''))
# #                 return base_price
# #             else:
# #                 print("Faqat 1 dan 5 gacha bo'lgan raqamlarni kiriting.")
# #         except ValueError:
# #             print("Faqat son kiriting!\n1,2,3,4,5")




# # def return_colors_price(base_price):
# #     print("""
# #     Available colors:
# #     1. Oq (0% extra money)
# #     2. Qora (3% extra money)
# #     3. Malla (2% extra money)
# #     """)

# #     color_price_adjustments = {
# #         "1": 0.0,
# #         "2": 0.03,
# #         "3": 0.02
# #     }

# #     while True:
# #         color_choice = input("Select a color by entering its number (1-3): ")
# #         if color_choice in color_price_adjustments:
# #             color_name = ["Oq", "Qora", "Malla"][int(color_choice) - 1]
# #             extra_percentage = color_price_adjustments[color_choice]
# #             final_price = base_price * (1 + extra_percentage)
# #             print(f"\nYou selected: {color_name}")
# #             print(f"Base Price: ${base_price:.2f}")
# #             print(f"Final Price (after color adjustment): ${final_price:.2f}\n")
# #             return final_price
# #         else:
# #             print("Please enter a valid number (1-3).")


# # def main():
# #     cars = Cars.get_cars()
# #     selected_car_type = find_car_type(cars)
# #     price = return_prices(selected_car_type)
# #     final_price = return_colors_price(price)
# #     print(f"Total Final Price: ${final_price:.2f}")
    
# #     while True:
# #         print('Tasdiqlaysizmi?')
# #         _input = input('>>>')
# #         if _input.lower() == 'ha':
# #             print("Sotib oldingiz\nSavdo tugadi")
# #             break
# #         elif _input.lower() == "yo'q":
# #             print("Savdo bekor qilindi")
# #         else:
# #             print("Iltimos faqat ha/yo'q kiriting")
# #             continue
        
            
# # if __name__ == "__main__":
# #     main()


# class Purchase:
#     def __init__(self):
#         self.cars = {
#             1: {"type": "Sedan", "models": [
#                 {"name": "Sedan Model A", "price": 20000},
#                 {"name": "Sedan Model B", "price": 22000},
#                 {"name": "Sedan Model C", "price": 25000}
#             ]},
#             2: {"type": "Hatchback", "models": [
#                 {"name": "Hatchback Model A", "price": 18000},
#                 {"name": "Hatchback Model B", "price": 19500},
#                 {"name": "Hatchback Model C", "price": 21000}
#             ]},
#             3: {"type": "Coupe", "models": [
#                 {"name": "Coupe Model A", "price": 27000},
#                 {"name": "Coupe Model B", "price": 30000},
#                 {"name": "Coupe Model C", "price": 35000}
#             ]},
#             4: {"type": "Minivan", "models": [
#                 {"name": "Minivan Model A", "price": 23000},
#                 {"name": "Minivan Model B", "price": 25000},
#                 {"name": "Minivan Model C", "price": 27000}
#             ]},
#             5: {"type": "SUV", "models": [
#                 {"name": "SUV Model A", "price": 30000},
#                 {"name": "SUV Model B", "price": 32000},
#                 {"name": "SUV Model C", "price": 35000}
#             ]}
#         }
#         self.colors = {
#             1: ("Black", 0.02),
#             2: ("White", 0.0),
#             3: ("Gray", 0.01)
#         }

#     def select_car(self):
#         print("Please select a car type from the following options:")
#         for key, car in self.cars.items():
#             print(f"{key}. {car['type']}")

#         while True:
#             try:
#                 car_choice = int(input("Enter the number: "))
#                 if car_choice in self.cars:
#                     selected_car = self.cars[car_choice]
#                     print(f"You have selected: {selected_car['type']}")
#                     return selected_car
#                 else:
#                     print("Invalid selection. Please try again.")
#             except ValueError:
#                 print("Please enter a valid number.")

#     def select_model(self, car):
#         print(f"\nAvailable models for {car['type']}:")
#         for index, model in enumerate(car['models'], start=1):
#             print(f"{index}. {model['name']} - ${model['price']}")

#         while True:
#             try:
#                 model_choice = int(input("Select a model by entering its number: "))
#                 if 1 <= model_choice <= len(car['models']):
#                     selected_model = car['models'][model_choice - 1]
#                     print(f"You have selected: {selected_model['name']}")
#                     return selected_model
#                 else:
#                     print("Invalid selection. Please try again.")
#             except ValueError:
#                 print("Please enter a valid number.")

#     def select_color(self):
#         print("\nAvailable colors:")
#         for key, (color, extra) in self.colors.items():
#             print(f"{key}. {color} with {extra * 100:.0f}% extra money")

#         while True:
#             try:
#                 color_choice = int(input("Select a color by entering its number: "))
#                 if color_choice in self.colors:
#                     selected_color, extra = self.colors[color_choice]
#                     print(f"You have selected: {selected_color}")
#                     return selected_color, extra
#                 else:
#                     print("Invalid selection. Please try again.")
#             except ValueError:
#                 print("Please enter a valid number.")

#     def confirm_purchase(self, car, model, color, base_price, final_price):
#         print("\nPlease confirm your selection:")
#         print(f"Type: {car['type']}")
#         print(f"Model: {model['name']}")
#         print(f"Color: {color}")
#         print(f"Base Price: ${base_price:.2f}")
#         print(f"Final Price (after color adjustment): ${final_price:.2f}")
#         while True:
#             confirm = input("Do you want to proceed with the purchase? (yes/no): ").lower()
#             if confirm == 'yes':
#                 print("\nPurchase confirmed!")
#                 print(f"\nProcessing payment...\nPayment of ${final_price:.2f} completed successfully!")
#                 print("Thank you for your purchase.")
#                 break
#             elif confirm == 'no':
#                 print("Purchase cancelled.\nNo purchase to complete.")
#                 break
#             else:
#                 print("Please enter just YES or NO")
#                 continue
                

#     def run(self):
#         selected_car = self.select_car()
#         selected_model = self.select_model(selected_car)
#         selected_color, extra = self.select_color()
        
#         base_price = selected_model['price']
#         final_price = base_price * (1 + extra)
        
#         self.confirm_purchase(selected_car, selected_model, selected_color, base_price, final_price)


# if __name__ == "__main__":
#     purchase = Purchase()
#     purchase.run()


cars = {
1: {"type": "Sedan", "models": [
    {"name": "Sedan Model A", "price": 20000},
    {"name": "Sedan Model B", "price": 22000},
    {"name": "Sedan Model C", "price": 25000}
]},
2: {"type": "Hatchback", "models": [
    {"name": "Hatchback Model A", "price": 18000},
    {"name": "Hatchback Model B", "price": 19500},
    {"name": "Hatchback Model C", "price": 21000}
]},
3: {"type": "Coupe", "models": [
    {"name": "Coupe Model A", "price": 27000},
    {"name": "Coupe Model B", "price": 30000},
    {"name": "Coupe Model C", "price": 35000}
]},
4: {"type": "Minivan", "models": [
    {"name": "Minivan Model A", "price": 23000},
    {"name": "Minivan Model B", "price": 25000},
    {"name": "Minivan Model C", "price": 27000}
]},
5: {"type": "SUV", "models": [
    {"name": "SUV Model A", "price": 30000},
    {"name": "SUV Model B", "price": 32000},
    {"name": "SUV Model C", "price": 35000}
]}}



def select_model(car):
    print(f"\nAvailable models for {car['type']}:")
    for index, model in enumerate(car['models'], start=1):
        print(f"{index}. {model['name']} - ${model['price']}")

    while True:
        try:
            model_choice = int(input("Select a model by entering its number: "))
            if 1 <= model_choice <= len(car['models']):
                selected_model = car['models'][model_choice - 1]
                print(f"You have selected: {selected_model['name']}")
                return selected_model
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")


print("Please select a car type from the following options:")
for key, car in cars.items():
    print(f"{key}. {car['type']}")


while True:
    try:
        car_choice = int(input("Enter the number: "))
        if car_choice in cars:
            selected_car = cars[car_choice]
            print(selected_car)
            print(f"You have selected: {selected_car['type']}")
            print(selected_car)
            selected_model = select_model(selected_car)
            break
        else:
            print("Invalid selection. Please try again.")
    except ValueError:
        print("Please enter a valid number.")

# print(cars)