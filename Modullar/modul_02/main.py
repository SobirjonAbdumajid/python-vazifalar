# import all_info_about_avtos

# car1 = all_info_about_avtos.give_info_about_avtos('gm','malibu','oq','avtomat',2022,45000)
# all_info_about_avtos.print_info_of_avtos(car1)



# import all_info_about_avtos as info

# car1 = info.give_info_about_avtos('tesla','tesla car','oq','avtomat','2023',34000)
# info.print_info_of_avtos(car1)



# from all_info_about_avtos import give_info_about_avtos,print_info_of_avtos
# from all_info_about_avtos import give_info_about_avtos as taker_info, print_info_of_avtos as print_info
from all_info_about_avtos import *

car1 = give_info_about_avtos('gm','malibu','qora','avtomat',2014,32000)
print_info_of_avtos(car1)

