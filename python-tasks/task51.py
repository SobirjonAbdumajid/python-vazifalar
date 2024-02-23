# def giveInfoOf_students(name, surename, **information):
#     '''this function gives information about students as a dictionary'''
#     information['name'] = name.title()
#     information['surename'] = surename.title()
#     return information

# print(giveInfoOf_students('sobirjon','abdumajidov',student_id = 23432, room_number = 231))

def talaba_info(ism, familiya, **kwargs):
    kwargs['ism']=ism
    kwargs['familiya']=familiya
    return kwargs

talaba = talaba_info('olim','olimov',tyil=1995,fakultet='IT',yonalish='AT')