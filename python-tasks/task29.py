# nomer = input('Nomer: ')
# alpha = ''

# for n in nomer:
#     if n.isalpha():
#         alpha+=n
# if alpha == 'ppp':
#     print('Jarimasiz.')
# else:    
#     print('jarima 33434$')



car_number = input('Nomer: ')
letter_part = ""

for charr in car_number:
    if charr.isalpha():
        letter_part += charr
        

if letter_part.lower() == 'vsf' or letter_part.lower() == 'ppp' or letter_part.lower() == 'xxx':
    print('Jarimasiz.')
else:
    print("Jarima 34234324324$")
