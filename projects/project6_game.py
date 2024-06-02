import random, sys
GameOver = ValueError

def random_number(start, end):
    return random.randint(start, end)


def check_number(number, guess):
    message = 'Men o\'ylagan son'
    if number < guess:
        return f'{message} {guess} dan kichikroq.'
    if number > guess:
        return f'{message} {guess} dan kattaroq. '
    raise GameOver

# def ask_question(response1):
#     start = 1
#     end = 10
#     if response1 == '-':
#         return
#     if response1 == '+':
#         return '+'
#     raise GameOver

def main(start, end):

    number = random_number(start, end)
    print('1 dan 10 gacha son o\'yladim. toping!: ')
    guess = int(input('Son: '))
    counter1 = 1

    while True:
        try:
            message = check_number(number, guess)
            print(message)
            guess = int(input('Son: '))
            counter1 += 1

        except GameOver:
            print(f'{counter1} ta urunishda topdingiz!')
            break
    input('1 dan 10 gacha son o\'ylang endi man topaman!')
    counter2 = 1

    while True:
        randomNumber = random_number(start, end)
        try:
            response = input(f'Siz {randomNumber} sonini o\'yladingiz!\n>>>')

            if response == '-':
                end = randomNumber - 1
            elif response == '+':
                start = randomNumber + 1
            else:
                raise GameOver
            counter2 += 1

            # print(finalResponse)
        except GameOver:

            final(counter2, counter1)
            break


def final(computer, human):
    answer1 = f'Man {computer} ta urunishda'
    answer2 = f'Siz {human} ta urunishda'
    if human < computer:
        print(answer1, answer2, 'topdingiz, Yutdingiz!')
    elif human > computer:
        print(answer2, answer1, 'topdim, Yutdim!')
    else:
        print(f'Durrang! Ikkalamiz {human} urunishda topdik.')

        
if __name__ == '__main__':
    main(1, 10)