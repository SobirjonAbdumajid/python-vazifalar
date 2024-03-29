import random
GameOver = ValueError

def random_number():
    return random.randint(1,10)

def check_number(number, guess):
    message = 'Men o\'ylagan son '
    if number < guess:
        return f'{message} {guess} dan kichikroq.'
    if number > guess:
        return f'{message} {guess} dan kattaroq. '
    raise GameOver

def main():
    number = random_number()
    print('1..10: ', number)
    guess = int(input('Son: '))
    counter = 1

    while True:
        try:
            if counter == 3:
                print('Siz 3 marta urindingiz va yutqizdingiz! ')
                break
            message = check_number(number, guess)
            print(message)
            guess = int(input('Son: '))
            counter+=1
            
        except GameOver:
            print('Topdingiz!')
            break
        
        
if __name__=='__main__':
    main()