# Homework Homework  Homework  Homework  Homework  Homework  Homework  Homework  Homework  Homework  Homework  Homework  Homework  Homework
import sys
products = {
    'limon':30000,
    'mandarin':35000,
    'anjir':20000,
    'nok':21000,
    'nashvoti':10000,
    'banan':23000,
    'tarvuz':25000,
    'qovun':35000,
    'handalak':32000,
    'tut':15000,
    'olma':10000,
    'shotut':27000,
    'olvali':14000,
    'olcha':20000,
    'kishmish':33000,
    'husayni':45000,
    'sultoni':36000,
    'o\'rik':24000,
    'shaftoli':22000,
    'mayz':39000,
    "yong'oq":28000,
    'ananas':26000,
    'dovcha':21000,
    'shkalat':17000,
    'perok':21000,
    'anor':20000,
    'kiwi':30000,
    'kodi':14000,
    'sabzi':13000,
    'kartoshka':6000,
    'piyoz':6000,
    'chisnok':5000,
    'qalampir':3000,
    'hurmo':12000,
    'tuxum':1000,
    'tvarok':13000,
    'qatiq':9000,
    'pamidor':23000,
}



saled_products = {}
values = []

print('Mahsulotlardan tanlang.')
for product in products:
    print(product+',',end=' ')
n = 1
print()
while True:
    product = input(f'{n} - mahsulot: ').lower()

    if product in products:
        amount = int(input('Nechi kg olmoqchisiz: '))
        price = products.get(product) * amount
        print(f'{price} bo\'ldi.')

        saled_products[product] = [amount,price]
    else:
        # print(f'Bizda {[product]} yo\'q.')
        print(f'Bizda bunday mahsulot yo\'q.')
        continue
    n += 1
    while True:
        response1 = input('Ya\'na mahsulot olasizmi? (ha/yo\'q)\n>>>').lower()
        if response1 == 'ha':
            break
        elif response1 == 'yo\'q':
            while True:    
                response3 = input('Sotib olgan mahsulotlaringizni ko\'rasizmi? (ha/yo\'q)\n>>>').lower()
                if response3 == 'ha':
                    for keys, values in saled_products.items():
                        print(f"{keys}:",end=' ')
                        for inlist in values:
                            print(inlist,end=' ')
                        print()
                    sys.exit()
                elif response3 == "yo'q":
                    print('Dastur tugadi!')
                    sys.exit()
                else:
                    print('Faqat ha/yo\'q deb javob bering!')   
        else:
            print('Faqat ha/yo\'q deb javob bering!')