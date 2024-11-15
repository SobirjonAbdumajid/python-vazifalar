class Car:
    def __init__(self, car_type, models):
        self.car_type = car_type
        self.models = models


class Model:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Purchase:
    def __init__(self):
        self.cars = {
            1: Car("Sedan", [
                Model("Sedan Model A", 20000),
                Model("Sedan Model B", 22000),
                Model("Sedan Model C", 25000)
            ]),
            2: Car("Hatchback", [
                Model("Hatchback Model A", 18000),
                Model("Hatchback Model B", 19500),
                Model("Hatchback Model C", 21000)
            ]),
            3: Car("Coupe", [
                Model("Coupe Model A", 27000),
                Model("Coupe Model B", 30000),
                Model("Coupe Model C", 35000)
            ]),
            4: Car("Minivan", [
                Model("Minivan Model A", 23000),
                Model("Minivan Model B", 25000),
                Model("Minivan Model C", 27000)
            ]),
            5: Car("SUV", [
                Model("SUV Model A", 30000),
                Model("SUV Model B", 32000),
                Model("SUV Model C", 35000)
            ])
        }
        self.colors = {
            1: ("Black", 0.02),
            2: ("White", 0.0),
            3: ("Gray", 0.01)
        }

    def select_car(self):
        print("Please select a car type from the following options:")
        for key, car in self.cars.items():
            print(f"{key}. {car.car_type}")

        while True:
            try:
                car_choice = int(input("Enter the number corresponding to your choice: "))
                if car_choice in self.cars:
                    selected_car = self.cars[car_choice]
                    print(f"You have selected: {selected_car.car_type}")
                    return selected_car
                else:
                    print("Invalid selection. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

    def select_model(self, car):
        print("\nAvailable models for", car.car_type + ":")
        for index, model in enumerate(car.models, start=1):
            print(f"{index}. {model.name} - ${model.price}")

        while True:
            try:
                model_choice = int(input("Select a model by entering its number: "))
                if 1 <= model_choice <= len(car.models):
                    selected_model = car.models[model_choice - 1]
                    print(f"You have selected: {selected_model.name}")
                    return selected_model
                else:
                    print("Invalid selection. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

    def select_color(self):
        print("\nAvailable colors:")
        for key, (color, extra) in self.colors.items():
            print(f"{key}. {color} with {extra * 100:.0f}% extra money")

        while True:
            try:
                color_choice = int(input("Select a color by entering its number: "))
                if color_choice in self.colors:
                    selected_color, extra = self.colors[color_choice]
                    print(f"You have selected: {selected_color}")
                    return selected_color, extra
                else:
                    print("Invalid selection. Please try again.")
            except ValueError:
                print("Please enter a valid number.")


    def confirm_purchase(self, car, model, color, base_price, final_price):
        print("\nPlease confirm your selection:")
        print(f"Type: {car.car_type}")
        print(f"Model: {model.name}")
        print(f"Color: {color}")
        print(f"Base Price: ${base_price:.2f}")
        print(f"Final Price (after color adjustment): ${final_price:.2f}")
        confirm = input("Do you want to proceed with the purchase? (yes/no): ").lower()
        if confirm == 'yes':
            print("\nPurchase confirmed!")
            print(f"\nProcessing payment...\nPayment of ${final_price:.2f} completed successfully!")
            print("Thank you for your purchase.")
        else:
            print("Purchase cancelled.\nNo purchase to complete.")

    def run(self):
        selected_car = self.select_car()
        selected_model = self.select_model(selected_car)
        selected_color, extra = self.select_color()
        
        base_price = selected_model.price
        final_price = base_price * (1 + extra)
        
        self.confirm_purchase(selected_car, selected_model, selected_color, base_price, final_price)


if __name__ == "__main__":
    purchase = Purchase()
    purchase.run()
