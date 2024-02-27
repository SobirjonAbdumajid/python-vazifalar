import random as r

def think_number():
    '''This function think one uncertion number'''
    print('I thought a number from 1 to 10, can you find it?')
    comp_number = r.randint(1,10)
    return comp_number



def find_comp_number(comp_number):
    '''This function accept estimate number'''
    counter = 1
    while True:
        input_number = int(input('>>>'))
        if comp_number == input_number:
            print(f'Well! you have found it in {counter} try.')

            return counter

        elif comp_number > input_number:
            print(f'Wrong! I thought number is bigger than {input_number}')
            counter+=1
        elif comp_number < input_number:
            print(f'Wrong! I thought the number is smaller than {input_number}')
            counter+=1
        else:
            print('Enter just number!')
    


def finding_your_number():
    ''''''
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

                return counter
                
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
        print(f'Score drow we both find in {user_attempt} attampt.')
    elif comp_attempt < user_attempt:
        print(f'I won, i have found it in {comp_attempt} attempts, but you found it in {user_attempt} attempts.')
    else:
        print(f'You won, i have found it in {comp_attempt} attempts, you found it in {user_attempt} attempts.')
    