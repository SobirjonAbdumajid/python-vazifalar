class User:
    def __init__(self, name, surename, cardNumber, balance = None):
        self.name = name
        self.surename = surename
        self.cardNumber = cardNumber
        self.balance = balance

def Register():
    counter = 0
    while True:
        counter += 1
        name = input('Name: ')
        surename = input('Surename: ')
        cardNumber = int(input('Card number: '))
        password = input('Password: ')
        if password != 'somsa':
            if counter == 3:
                break
            continue
        else:
                break
    user = User(name, surename, cardNumber)
    return user
 

def ShowMenu():
    print('''1. Register.
             2. ''')


def checkBalance():
    return
    print('''1. ''')
user = Register()
print(user)





# import sys

# class Person():
#     def __init__(self,name,surename,age,balance):
#         self.name = name
#         self.surename = surename
#         self.age = age
#         self.balance = balance
#         # password

#     def get_balance(self):
#         return self.balance    


# def give_options():
#     print(f'1. Balance tekshirish.\n2. Pul yichish.\n3. Hisob to\'ldirish.\n4. exit')
#     choice = int(input('Tanlang: '))

#     return choice


# def check_options(options,balance): 
#     if options == 4:
#         print('Dastur tugadi!')       
#         sys.exit()
    
#     elif options == 1:
#             print(f'Sizning balansingiz: {balance}')
#     elif options == 2:
#         value = float(input('Qancha pul yichmoqchisiz: '))
#         if balance <= value:
#             print('Yitarli mablag\' mavjud emas!')
#         else:
#             print(f'{value} so\'m muvoffaqiyatli yichildi.')
        
#     elif options == 3:
#         addMoney = float(input('Qancha pul qo\'shmoqchisiz?\n>>>'))
#         print(f'{addMoney} so\'m pul muvoffaqiyatli qo\'shildi!')
#         balance+=addMoney
#     else:
#         print('Faqat 1/2/3/4 sonlarni kiriting!')

    
#         # give_options()
#     # check_result()
#     # return options


# def check_result():
#     while True:
#         response = input('Ya\'na xizmatdan foydalanasizmi: ').lower()
#         if response == 'ha':
#             print
#             # result = give_options()
#         elif response == 'yo\'q':
#             print('Dastur tugadi!')
#             sys.exit()
#         else:
#             print('Faqat ha/yo\'q deb javob bering!')


# def enter():
#     while True:
#         name = input('Ism: ')
#         surename = input('Surename: ')
#         age = int(input('Age: '))
#         # email = 
        
#         if age < 18:
#             print(f'Siz {age} yoshdasiz va bank xizmatlaridan foydalanish huquqiga ega emassiz.')
#             continue
#         # else:
#         user = Person(name,surename,age,balance = 0)

#         def player():
               
#                 option = give_options()
#                 balance = user.get_balance()
#                 check_options(option,balance)
#                 check_result()
            

# if __name__=='__main__':
#     enter()
        
        

        
       
       

# # 1-odam uchun tepadagi hizmatlar keyin ya'na 2-odam uchun ham o'zi hizmat ko'rsatishni boshlaydi. email password registratsiya
# # registratsiya qilish
# # 
