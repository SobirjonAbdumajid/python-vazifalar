# listlarni alifbo tartibida tartiblash-----------------------------------------------------------------------------------------

# cars = ['chevrolet','audi','mercedez benz','tesla','bmw']
# print(cars)

# print(cars[1:2])

# cars.sort() # sort metodi elementlarni tartiblab beradi
# print(cars)

# cars.sort(reverse=True) # reverse=True elementlarni teskari tartiblab beradi
# print(cars)

# print(sorted(cars)) #sorted faqat print qigincha ishlaydi. sortga o'hshaydi
# print(sorted(cars,reverse=True))

# sonlar = [3,6,-3,3,335,2,12,443,-342]
# print(sonlar)

# print(sorted(sonlar))
# print(sorted(sonlar,reverse=True))

# print(sonlar)
# sonlar.sort()
# print(sonlar)

# sonlar.sort(reverse=True) 
# print(sonlar)

# sonlar.reverse()
# print(sonlar)

# print(len(sonlar)) # len metodi list elementlarini sonini ko'rsatadi

# raqamlar = list(range(0,10)) # list va range yordamida ma'lum bir sonlar oralig'idagi list qiymatlarini chiqarsa bo'ladi

# print(raqamlar)
# print(list(range(10,33)))

# juft_sonlar = list(range(0,33,2))
# print(juft_sonlar)

# toq_sonlar = list(range(1,33,2))
# print(toq_sonlar)

# sanash = list(range(0,101,10))
# print(sanash)

# print(max(sanash)) # max sonlar ichidagi eng kattasini topib beradi
# print(min(sanash)) # min sonlar ichidagi eng kichkinasini topib beradi

# print(sum(toq_sonlar))
# print(sanash[0:3]) # bu orqali (sanash[0:3]) elementlarni ma'lum bir indexidan boshqa elementlarigacha ekranga chiqarish mumkin

# my_cars = ['volvo', 'bmw', 'mercedez benz']
# cars = my_cars[:] # [:] bu belgi bilan tenglangan elemenlarni birini o'zgartirsam faqat uzi o'zgaradi
# cars = my_cars[] # [:] bu belgisiz o'zgaruvchilarning birini qiymatini o'zgartirsam o'zgaruvchilar bir biriga tenglangan bo'lsa ikkinchisi ham o'zgarib ketadi
# print(cars,'\n',my_cars)

# my_cars.remove('volvo')
# print(my_cars,'\n',cars)







                       # tuple bilan listning farqi listni o'zgartirsa bo'ladi lekin tupleni o'zgartirib bo'lmaydi








toys = ('bus','car','bear','dino')

toys = list(toys) # bu usul bilan o'zgarmas tupleni listga aylantirib o'zgartirsa bo'ladi

toys = tuple(toys)

print(type(toys))
toys.remove('bus')
print(toys)