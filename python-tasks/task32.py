davlatlar = {
    'o\'zbekiston':{'poytaxti':'toshkent',
                    'hududi':448978,
                    'aholisi':33000000,
                    'pul birligi':'so\'m'},

    'rossiya':{'poytaxti':'moskva',
                    'hududi':17098246,
                    'aholisi':144000000,
                    'pul birligi':'rubl'},

    'aqsh':{'poytaxti':'vashington',
                    'hududi':9631418,
                    'aholisi':327000000,
                    'pul birligi':'dollar'},
    
    'malayziya':{'poytaxti':'kuala-lumpur',
                    'hududi':329750,
                    'aholisi':25000000,
                    'pul birligi':'rinngit'}
}

for davlat, malumot in davlatlar.items():
    if davlat.lower() == 'aqsh':
        print(davlat.upper())
    else:
        print(davlat.capitalize())
    print(f'\n{davlat.capitalize()}ning poytaxti {malumot['poytaxti'].title()}\nHududi: {malumot['hududi']} km kv\nAholisi: {malumot['aholisi']}\nPul birligi: {malumot['pul birligi']}')

# davlat = input('Qaysi davlat haqida ma\'lumot olmoqchisiz: ').lower()

# if davlat in davlatlar.keys():
#     for k, v in davlatlar[davlat].items():
#         print(f'{davlat.capitalize()}ning {k} {v}')
# else:
#     print(davlat + ' davlati haqida biz ma\'lumotga ega emasmiz.')



# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
#     }

# for davlat, info in davlatlar.items():
#     if davlat.lower()=='aqsh':
#         davlat = davlat.upper()
#     else:
#         davlat = davlat.capitalize()
#     print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['maydon']} kv.km"
#           f"\nAholisi: {info['aholi']}"
#           f"\nPul birligi: {info['pul birligi']}")
    


davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
    }

davlat = input('Davlat nomini kiriting: ').lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi: {info['maydon']} kv.km"
          f"\nAholisi: {info['aholi']}"
          f"\nPul birligi: {info['pul birligi']}")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")