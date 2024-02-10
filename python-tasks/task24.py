python_izohli_lugati = {'string':'satr',
                        'boolean':'mantiqiy qiymat',
                        'integer':'butun son',
                        'for':'biror amalni qayta takrorlash tsikli',
                        'if':'shart tekshirish operatori',
                        'float':'haqiqiy son',
                        'while':'qayta aylanuvchi tsikl',
                        'print':'chop etish',
                        'keys()':'lug\'atni kalit so\'zi',
                        'values()':'lug\'atni qiymati'}

for k, v in sorted(python_izohli_lugati.items()):
    print(f'{k.title()} - {v.capitalize()}')