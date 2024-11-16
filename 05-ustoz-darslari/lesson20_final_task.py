class Purchase:
    def __init__(self):
        self.cars = {
            1: {"type": "Sedan", "models": [
                {"name": "Toyota Camry", "price": 25000},
                {"name": "Honda Accord", "price": 26500},
                {"name": "Mazda6", "price": 27000},
                {"name": "BMW 3 Series", "price": 41500},
                {"name": "Mercedes-Benz C-Class", "price": 43000}
            ]},
            2: {"type": "Hatchback", "models": [
                {"name": "Volkswagen Golf", "price": 23500},
                {"name": "Ford Focus", "price": 22000},
                {"name": "Hyundai i30", "price": 24000},
                {"name": "Honda Civic Hatchback", "price": 25500},
                {"name": "Mazda3 Hatchback", "price": 26000}
            ]},
            3: {"type": "Coupe", "models": [
                {"name": "Ford Mustang", "price": 55000},
                {"name": "Chevrolet Camaro", "price": 50000},
                {"name": "BMW 4 Series", "price": 52000},
                {"name": "Audi A5", "price": 53500},
                {"name": "Mercedes-Benz C-Class Coupe", "price": 54000}
            ]},
            4: {"type": "Minivan", "models": [
                {"name": "Honda Odyssey", "price": 33500},
                {"name": "Toyota Sienna", "price": 34500},
                {"name": "Chrysler Pacifica", "price": 36000},
                {"name": "Kia Carnival", "price": 32500},
                {"name": "Dodge Grand Caravan", "price": 31500}
            ]},
            5: {"type": "SUV", "models": [
                {"name": "Toyota RAV4", "price": 29500},
                {"name": "Honda CR-V", "price": 28500},
                {"name": "Ford Explorer", "price": 36500},
                {"name": "Chevrolet Tahoe", "price": 49000},
                {"name": "Jeep Grand Cherokee", "price": 47500}
            ]}
        }
        self.colors = {
            1: ("Black", 0.02),
            2: ("White", 0.0),
            3: ("Gray", 0.01)
        }

    def select_car(self):
        print("Iltimos moshina turini tanlang:")
        
        for key, car in self.cars.items():
            print(f'{key}. {car['type']}')
        
        while True:
            user_car = int(input('Raqam kiriting: '))
            if user_car
        # print("Please select a car type from the following options:")
        # for key, car in self.cars.items():
        #     print(f"{key}. {car['type']}")
        # while True:
        #     try:
        #         car_choice = int(input("Enter the number: "))
        #         if car_choice in self.cars:
        #             selected_car = self.cars[car_choice]
        #             print(f"You have selected: {selected_car['type']}")
        #             return selected_car
        #         else:
        #             print("Invalid selection. Please try again.")
        #     except ValueError:
        #         print("Please enter a valid number.")

    def select_model(self, car):
        print("Iltimos moshina turini tanlang:")
        
        # for key, model in self        
        
        # print(f"\nAvailable models for {car['type']}:")
        # for index, model in enumerate(car['models'], start=1):
        #     print(f"{index}. {model['name']} - ${model['price']}")
        # while True:
        #     try:
        #         model_choice = int(input("Select a model by entering its number: "))
        #         if 1 <= model_choice <= len(car['models']):
        #             selected_model = car['models'][model_choice - 1]
        #             print(f"You have selected: {selected_model['name']}")
        #             return selected_model
        #         else:
        #             print("Invalid selection. Please try again.")
        #     except ValueError:
        #         print("Please enter a valid number.")

    def select_color(self):
        pass
        
        
        # print("\nAvailable colors:")
        # for key, (color, extra) in self.colors.items():
        #     print(f"{key}. {color} with {extra * 100:.0f}% extra money")
        # while True:
        #     try:
        #         color_choice = int(input("Select a color by entering its number: "))
        #         if color_choice in self.colors:
        #             selected_color, extra = self.colors[color_choice]
        #             print(f"You have selected: {selected_color}")
        #             return selected_color, extra
        #         else:
        #             print("Invalid selection. Please try again.")
        #     except ValueError:
        #         print("Please enter a valid number.")

    def confirm_purchase(self, car, model, color, base_price, final_price):
        pass
        
        
        # print("\nPlease confirm your selection:")
        # print(f"Type: {car['type']}")
        # print(f"Model: {model['name']}")
        # print(f"Color: {color}")
        # print(f"Base Price: ${base_price:.2f}")
        # print(f"Final Price (after color adjustment): ${final_price:.2f}")
        # while True:
        #     confirm = input("Do you want to proceed with the purchase? (yes/no): ").lower()
        #     if confirm == 'yes':
        #         print("\nPurchase confirmed!")
        #         print(f"Processing payment...\nPayment of ${final_price:.2f} completed successfully!")
        #         print("Thank you for your purchase.")
        #         break
        #     elif confirm == 'no':
        #         print("Purchase cancelled. No purchase to complete.")
        #         break
        #     else:
        #         print("Please enter just YES or NO")
        #         continue

    def run(self):
        selected_car = self.select_car()
        # selected_model = self.select_model(selected_car)
        # selected_color, extra = self.select_color()
        # base_price = selected_model['price']
        # final_price = base_price * (1 + extra)
        # self.confirm_purchase(selected_car, selected_model, selected_color, base_price, final_price)

if __name__ == "__main__":
    purchase = Purchase()
    purchase.run()
