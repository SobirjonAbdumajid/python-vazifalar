# def mark_students(names):
#     scoreOfstudents = {}
#     n = 0
#     while True:
#         for name in names:
#             mark = int(input(f'Enter {name.title()}\'s score: '))
#             scoreOfstudents[name] = int(mark)
#             n+=1
#             if n == len(names):
#                 return scoreOfstudents


# students = ['sobirjon','sardor','abduqahhor','abbos']
# mark_Of_students = mark_students(students)
# print(mark_Of_students)
# print(students)

talabalar = ['ali', 'vali', 'hasan', 'husan']

def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar
        
baholar = bahola(talabalar)
print(baholar)
print(talabalar)