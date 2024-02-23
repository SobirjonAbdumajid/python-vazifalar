'''
Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, 
perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing
'''
def find_r_p_d_a(radius):
    '''Aylananing radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya'''
    results = {
        'radiusi':radius,
        'diameteri':radius*2,
        'perimetri':2*3.14*radius,
        'yuzi':3.14 * radius ** 2
    }
    return results    


results = find_r_p_d_a(float(input('Radius: ')))
for keys, values in results.items():
    print(f'Aylananing {keys} {values} ga teng.')