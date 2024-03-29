import random as r,sys
def think_number():
    print('I thought a number from 1 to 10, can you find it?')
    comp_number = r.randint(1,10)
    find_comp_number(comp_number)



def find_comp_number(comp_number):
    counter = 1
    while True:
        input_number = int(input('>>>'))
        if comp_number == input_number:
            print(f'Well! you have found it in {counter} try.')
            finding_your_number(counter)
        elif comp_number > input_number:
            print(f'Wrong! I thought number is bigger than {input_number}')
            counter+=1
        elif comp_number < input_number:
            print(f'Wrong! I thought the number is smaller than {input_number}')
            counter+=1
        else:
            print('Enter just number!')
    


def finding_your_number(user_attempts):
    counter = 1
    while True:
        print('Think number from 1 to 10. If you have thought number')    
        input('click any button! ')
        start = 1
        end = 10
        while True:
            comp_try_number1 = r.randint(start,end)
            print(f'Have you thought {comp_try_number1}.')
            response = input(f'Did i find it (yes), if number bigger than {comp_try_number1} click (+), or wise wersa click (-): ').lower()
            if response == 'yes':
                print(f'Well! I found it in {counter} try.')
                compare_of_attempts(counter, user_attempts)
                sys.exit()
                
            elif response == '-':
                end = comp_try_number1-1
                counter += 1
            elif response == '+':
                start = comp_try_number1+1
                counter += 1
            else:
                print('Enter just -/+')



def compare_of_attempts(comp_attempt, user_attempt):
    if comp_attempt == user_attempt:
        print(f'Scare drow we both find in {user_attempt} attampt.')
    elif comp_attempt < user_attempt:
        print(f'I won, i have found it in {comp_attempt} attempt, but you found it in {user_attempt} attempt.')
    else:
        print(f'You won, i have found it in {comp_attempt} attempt, you found it in {user_attempt} attempt   .')



if __name__ == '__main__':
    think_number()

"""
08/01/2021

Dasturlash asoslari

"SONNI TOPISH" O'YINI

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
# import random

# def sontop(x=10):
#     tasodifiy_son = random.randint(1,x)
#     print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?", end="")
#     taxminlar = 0
#     while True:
#         taxminlar += 1
#         taxmin = int(input(">>>"))
#         if taxmin<tasodifiy_son:
#             print("Xato. Men o'ylagan son bundan kattaroq. Yana harakat qiling:", end="")
#         elif taxmin>tasodifiy_son:
#             print("Xato. Men o'ylagan son bundan kichikroq. Yana harakat qiling:", end="")
#         else:
#             break
        
#     print(f"Tabriklayman. {taxminlar} ta taxmin bilan topdingiz!")
#     return taxminlar
    

# def sontop_pc(x=10):
#     input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
#     quyi = 1
#     yuqori = x
#     taxminlar = 0
#     while True:
#         taxminlar += 1
#         if quyi != yuqori:
#             taxmin = random.randint(quyi,yuqori)
#         else:
#             taxmin = quyi
#         javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
#                       f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
#         if javob == "-":
#             yuqori = taxmin - 1
#         elif javob == "+":
#             quyi = taxmin + 1
#         else:
#             break
#     print(f"Men {taxminlar} ta taxmin bilan topdim!")
#     return taxminlar

# def play(x=10):
#     yana = True
#     while yana:
#         taxminlar_user = sontop(x)
#         taxminlar_pc = sontop_pc(x)
        
#         if taxminlar_user>taxminlar_pc:
#             print(f"Men {taxminlar_pc} taxmin bilan topdim va  yutdim!")
#         elif taxminlar_user<taxminlar_pc:
#             print(f"Siz {taxminlar_user} taxmin bilan topdingiz va yutdingiz!")
#         else:
#             print("Durrang!")
#         yana = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0):"))
            
# play()