class Student:
    # def __init__(self, name,surename,age):
    #     self.ism = name
    #     self.familiya = surename
    #     self.yosh = age

    def __init__(self, name,surename,age):
        self.name = name
        self.surename = surename
        self.age = age

    def get_name(self):
        return self.name.title()
    
    def get_age(self,t_year):
        return t_year - self.age
    
    def get_surename(self):
        return self.surename

    def introduce(self):
        return f'Your name: {self.name} and surename: {self.surename}, you are {self.age} year old.'

student1 = Student('sobirjon','abdumajidov',18)
student2 = Student('sardor','odiljonov',21)
student3 = Student('abbos','umedov',19)

print(student2.get_age(2024))


print(student1.get_name())

# result = student1.introduce()
# print(result)

















# print(student1.name.title())
# print(student1.surename.title())
# print(student1.age)