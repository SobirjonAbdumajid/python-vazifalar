class Person():
    def __init__(self,name,surename,age,balance,password,email):
        self.name = name
        self.surename = surename
        self.age = age
        self.balance = balance
        password

    def get_balance(self):
        return self.balance    
    
if __name__ == '__main__':
    
    name = input('Ism: ')
    surename = input('Surename: ')
    age = int(input('Age: '))
    
    print(f'1. Balance tekshirish.\n2. Pul yichish.\n3. Hisob to\'ldirish.')
    
    choice = int(input('Tanlang: '))

    user = Person(name,surename,age,balance = 0)
    balance = user.get_balance()
    if choice == 1:
        print(user.get_balance())
    elif choice == 2:
        value = float(input('Qancha pul yichmoqchisiz: '))
        if balance <= value:
            print('Yitarli mablag\' mavjud emas!')
        else:
            print(f'{value} so\'m muvoffaqiyatli yichildi.')
    elif choice == 3:
        addMoney = float(input('Qancha pul qo\'shmoqchisiz?\n>>>'))
        print(f'{addMoney} so\'m pul muvoffaqiyatli qo\'shildi!')
        balance+=addMoney
    else:
        print('Faqat 1/2/3 kiritishingiz mumkin')

# 1-odam uchun tepadagi hizmatlar keyin ya'na 2-odam uchun ham o'zi hizmat ko'rsatishni boshlaydi. email password registratsiya
# registratsiya qilish
# 
