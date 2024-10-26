def give_info_about_avtos(kompaniya, model, color, box, year, price = None):
    '''Avtomabillar haqida ma\'lumotlar beruvchi funksiya'''
    avto = {
        'kompaniya':kompaniya,
        'model':model,
        'color':color,
        'box':box,
        'year':year,
        'price':price
    }
    return avto



def input_info_about_avto():
    cars = []
    while True:
        print('Quyidagi ma\'lumotlarni to\'ldiring!')
        kompaniya = input('Ishlab chiqaruvchi: ')
        model = input('Modeli ')
        color = input('Rangi: ')
        box = input('Karobka: ')
        year = input('Ishlab chiqarilgan yili: ')
        price = input('Narhi: ')
        
        cars.append(give_info_about_avtos(kompaniya,model,color,box,year,price))

        response = input('Wonna add car again (yes/no): ')
        if response == 'no':
            break
        return cars

def print_info_of_avtos(cars):
    '''This function prints information about cars'''
    print(f'{cars['year']} - yil {cars['kompaniya'].upper()}da ishlab chiqarilgan {cars['color']} rangli {cars['box']} karobka {cars['model']}ning narxi {cars['price']}$')
    
    

