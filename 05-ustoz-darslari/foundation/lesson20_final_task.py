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
            1: ("Black", 0.2),
            2: ("White", 0.0),
            3: ("Gray", 0.1)
        }

    def select_car(self):
        print("Iltimos moshina turini tanlang:")
        
        for key, car in self.cars.items():
            print(f'{key}. {car['type']}')
        
        while True:
            try:
                option_car = int(input('Raqam kiriting: '))
                user_car = self.cars[option_car]
                print(f'{user_car['type']}\'ni tanladingiz!' )
                return user_car
            except:
                print('Iltimos, yaroqli raqam kiriting')
                continue

    def select_model(self, car):
        print("Iltimos moshina turini tanlang:")
        
        for index, model in enumerate(car['models'], start=1):
            print(f'{index}. {model['name']} - ${model['price']}')
        
        while True:
            
            try:
                option_car = int(input("Tanlang: "))
                user_model = car['models'][option_car - 1]
                print(f'{user_model['name']}\'ni tanladingiz!')
                return user_model
            except:
                print('Iltimos, yaroqli raqam kiriting')
                continue

    def select_color(self):
        for key, (color, extra) in self.colors.items():
            print(f'{key}. {color} - {extra}% qo\'shimcha')
        
        while True:
            try:
                option_color = int(input('Tanlang: '))
                user_color, extra_price = self.colors[option_color]
                print(f'{user_color}\'ni tanladingiz!')
                return option_color, extra_price
            except:                
                print('Iltimos, yaroqli raqam kiriting')
                continue

    def confirm_purchase(self, car, model, color, base_price, final_price):
        print(f"Type: {car['type']}")
        print(f"Model: {model['name']}")
        print(f"Color: {color}")
        print(f"Final price: {final_price:.2f}")
        
        while True:
            confirm = input("Xarid qilasizmi? (ha/yo'q): ").lower()
            if confirm == 'ha':
                print("\nXarid tasdiqlandi!")
                print("Xaridingiz uchun rahmat.")
                break
            elif confirm == 'yo\'q':
                print("Xarid bekor qilindi!")
                break
            else:
                print("Faqat HA yoki YO‘Q deb kiriting")
                continue
        
    def run(self):
        selected_car = self.select_car()
        selected_model = self.select_model(selected_car)
        selected_color, extra_price = self.select_color()
        base_price = selected_model['price']
        final_price = base_price * (1 + extra_price)
        self.confirm_purchase(selected_car, selected_model, selected_color, base_price, final_price)

if __name__ == "__main__":
    purchase = Purchase()
    purchase.run()
