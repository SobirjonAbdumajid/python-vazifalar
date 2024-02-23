def mark_students(names):
    scoreOfstudents = {}
    while names:
        student_name = names.pop()
        mark = int(input(f'Enter {student_name.title()}\'s score: '))
        scoreOfstudents[student_name] = int(mark)
    return scoreOfstudents

students = ['sobirjon','sardor','abduqahhor','abbos']
mark_Of_students = mark_students(students[:])
print(mark_Of_students)
print(students)



# def find_sum(*numbers):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     total = 0
#     for number in numbers:
#         total+=number
#     return total
# print(find_sum(1,3,3))


# def find_sum(*numbers):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return sum(numbers)

# print(find_sum(1,3,3))


# def find_summa(n1,n2,*n3): # agar *n3 bitta * belgisi tuple sifatida qiymatlarni qabul qiladi.
#     result = n1,n2,n3
#     return result
# print(find_summa(1,2,'3','1',3,'asdfa5','63')) 



# def avto_info(kompaniya, model, **information): # ikkita ** belgi (**information) lug'at ko'rinishida qabul qiladi
#     '''Avtomobilar haqidagi ma\'lumotlarni lug\'at ko\'rinishida qaytaruvchi funksiya'''
#     # information['kompaniyasi'] = kompaniya
#     # information['model'] = model.title()
#     return information
# print(avto_info('gm','malibu',yil = 2018,narx = 35000))

print(0.1+0.2)