# # # 1
# # class MyNumbers:
# #     def __iter__(self):
# #         self.current = 2  # Boshlanish nuqtasini belgilaymiz
# #         return self  # O'zini qaytaradi, bu - qutini ochib qo'yish
       
# #     def __next__(self):
# #         if self.current <= 5:  # Agar hali 5 ga yetmagan bo'lsa
# #             number = self.current  # Hozirgi raqamni saqlab olamiz
# #             self.current += 1  # Keyingi safar uchun raqamni oshiramiz
# #             return number  # Raqamni qaytaradi
# #         else:
# #             raise StopIteration  # Agar qutidagi barcha shirinliklar tamom bo'lsa, to'xtatadi

# # # Obyektni yaratamiz
# # numbers = MyNumbers()

# # # Qutini ochib, ichidan bittadan shirinlik olamiz
# # for num in numbers:
# #     print(num)


# # # 2
# # class Oyinchilar:
# #     def __init__(self, royxat):
# #         self.royxat = royxat

# #     def __iter__(self):
# #         self.index = 0  # Boshlanish nuqtasi
# #         return self

# #     def __next__(self):
# #         if self.index < len(self.royxat):
# #             element = self.royxat[self.index]
# #             self.index += 1
# #             return element
# #         else:
# #             raise StopIteration  # Oyinchilar tugaganda xatolik chiqaradi

# # # Oyinchilarni royxatini yaratamiz
# # oyinchilar = Oyinchilar(["Mario", "Luigi", "Peach", "Toad"])

# # # Endi ularni bitta-bitta oqiymiz
# # for oyinchi in oyinchilar:
# #     print(oyinchi)



# # # 3
# # class MyBag:
# #     def __init__(self, items):
# #         self.items = items

# #     def __iter__(self):
# #         self.index = 0  # boshlanish nuqtasi
# #         return self

# #     def __next__(self):
# #         if self.index < len(self.items):
# #             result = self.items[self.index]  # navbatdagi shirinlik
# #             self.index += 1  # keyingi indeksga o‘tish
# #             return result
# #         else:
# #             raise StopIteration  # oxiriga yetganimizni bildiradi

# # my_bag = MyBag(['olma', 'banan', 'gilos'])

# # for item in my_bag:
# #     print(item)



# # # 4
# # class MyIterator:
# #     def __init__(self, max_value):
# #         self.max_value = max_value
# #         self.current = 0

# #     def __iter__(self):
# #         self.current = 0  # Boshlanish nuqtasini o'rnatamiz
# #         return self

# #     def __next__(self):
# #         if self.current < self.max_value:
# #             result = self.current
# #             self.current += 1
# #             return result
# #         else:
# #             raise StopIteration  # Elementlar tugaganda xatolik chiqaradi

# # # MyIterator obyekti
# # my_iter = MyIterator(5)

# # # Bu obyekt endi iterable bo‘lgani uchun `for` tsiklida foydalanish mumkin
# # for num in my_iter:
# #     print(num)



# # # 5
# # class MyIterator:
# #     def __iter__(self):
# #         self.current = 1  # Boshlanish nuqtasini o‘rnatamiz
# #         return self

# #     def __next__(self):
# #         if self.current <= 3:
# #             result = self.current
# #             self.current += 1
# #             return result
# #         else:
# #             raise StopIteration  # Elementlar tugaganda to‘xtatish uchun xato chiqaradi

# # # MyIterator obyekti
# # my_iter = MyIterator()

# # # `for` tsiklida foydalanamiz
# # for num in my_iter:
# #     print(num)



# # # 6
# # class Counter:
# #     def __init__(self):
# #         self.current = 1  # Boshlanish nuqtasini o'rnatamiz

# #     def __next__(self):
# #         if self.current <= 3:
# #             result = self.current
# #             self.current += 1
# #             return result
# #         else:
# #             print("raise StopIteration  # To'xtatish uchun xato chiqaradi")

# # # Counter obyekti
# # counter = Counter()

# # # `next()` yordamida qiymatlarni chiqaramiz
# # print(next(counter))  # 1
# # print(next(counter))  # 2
# # print(next(counter))  # 3
# # # print(next(counter))  # StopIteration chiqariladi


# # # 7
# # class MyNext:
# #     def __init__(self):
# #         self.current = 1
        
# #     def __iter__(self):
# #         return self
    
# #     def __next__(self):
# #         if self.current <= 4:
# #             result = self.current
# #             self.current += 1
# #             return result
        
# # my_next = MyNext()

# # for i in my_next:
# #     print(i)

# # print(next(my_next))
# # print(next(my_next))
# # print(next(my_next))
# # print(next(my_next))



# # 8
# # from typing import override
# # class Human:
# #     def voice(self):
# #         raise NotImplementedError(self.__class__.__name__)

# # class Teacher(Human):
# #     def __init__(self, name: str):
# #         self.name = name
    
# #     def voice(self):
# #         print('Maladest\nbali')

    
# # class Student(Human):
# #     def __init__(self, name):
# #         self.name = name
# #     def voice(self):
# #         print('Ustoooz\nKechiring')
        
# # class Diractor(Human):
# #     def __init__(self, name: str):
# #         self.name = name
        
# #     def voice(self):
# #         print("bo'shadin")

# # teacher1 = Teacher('Ustoz1')
# # teacher2 = Teacher('Ustoz2')
# # student1 = Student('Talaba1')
# # student2 = Student('Talaba2')
# # student3 = Student('Talaba3')
# # diractor1 = Student('Talaba3')

# # list_of_human = [teacher1, teacher2, student1, student2, student3, diractor1]

# # for h in list_of_human:
# #     h.voice()



# class Animals:
#     def move(self):
#         raise NotImplementedError(self.__class__.__name__)
    
#     def voice(self):
#         raise NotImplementedError(self.__class__.__name__)

    

# class Cat(Animals):    
#     def move(self):
#         print("walk")
    
#     def voice(self):
#         print('Miyov')


# class Dog(Animals):    
#     def move(self):
#         print("run")
    
#     def voice(self):
#         print('vov')
    
# class Bird(Animals):   
#     def move(self):
#         print("fly")
    
#     def voice(self):
#         print('chirq')


# def animal_behaviour(animals: list[Animals]):
#     for a in animals:
#         a.voice()
#         a.move()


# list_of_animals = [Bird(), Cat(), Dog()]

# animal_behaviour(list_of_animals)
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
                return user_color, extra_price
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
