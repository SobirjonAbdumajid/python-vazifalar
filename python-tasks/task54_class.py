'''
Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. Klassning 
xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab 
qiladigan ma'lumotlarni kiriting (ism, foydalanuvchi ismi, email, va hokazo)
'''

'''
Klassga bir nechta metodlar qo'shing, jumladan get_info() 
metodi foydalanuvchi haqida yig'ilgan ma'lumotlarni 
chiroyli qilib chiqarsin (masalan: "Foydalanuvchi: 
alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).
'''

'''
Klassdan bir nechta obyektlar yarating va uning 
xususiyatlari va metodlariga murojat qiling.
'''

class User:
    def __init__(self,name,surename,email,password):
        self.name = name
        self.surename = surename
        self.email = email
        self.password = password

    def registration(self):
        return f'{self.email} and {self.password} are {self.name.title()} {self.surename.title()}\'s email and password'


if __name__=='__main__':
    # name = input('Ism: ')
    # surename = input('Surename: ')
    # email = input('Email: ')
    # password = input('Password: ')

    person1 = User('sobirjon', 'abdumajidov','re.fire761@gmail.com','onamotam')
    print(person1.registration())

    person2 = User('sardor','odilov','sardorodilov@gmail.com','odilov')
    print(person2.registration())

    person3 = User('abbos','ergashev','abbosergashev@gamil.com','ergashev')
    print(person3.registration())