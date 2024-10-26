from words import words
import random as r
def choose_word():
    random_word = r.choice(words)
    while ' ' in random_word or '-' in random_word:
        random_word = r.choice(words)
        
    return random_word.upper()

def find_number(random_word):
    length = len(random_word)
    print(f'\nI thought of a {length} letter word can you find it?', random_word)

    counter = 0
    all_letters = []

    abstract = []
    for l in random_word:
        abstract.append('_')

    list_random_word = []
    for rd in random_word:
        list_random_word.append(rd)

    for abs in abstract:
        print(abs,end='')

    while True:

        input_letter = input('\n\nEnter letter: ').upper()
        counter += 1
        if input_letter in all_letters:
            print(f'Letter {input_letter} is already entered, enter other letter!')
            continue
        all_letters.append(input_letter)

        if input_letter in list_random_word:

            for ind in range(len(list_random_word)):
                if list_random_word[ind] == input_letter:
                    abstract[ind] = input_letter

            print(f'\nYou have found it, letter {input_letter} is in the word.')
            if abstract == list_random_word:
                print(f'Well done! you have found word {random_word.upper()} in {counter} try')
                break
            for abs in abstract:
                print(abs,end='')

        else:
            print(f'\nLetter {input_letter} is not in the word!')
            for abs in abstract:
                print(abs,end='')
        
        print('\nLetters you have enterd so far: ',end='')
        for all_letter in all_letters:
            print(all_letter,end='')
        
        if abstract == list_random_word:
            break

def play():
    random = choose_word()
    result = find_number(random)
    print(result)





# import random
# from uzwords import words

# def get_word():
#     word = random.choice(words)
#     while "-" in word or ' ' in word:
#         word = random.choice(words)    
#     return word.upper()

# def display(user_letters,word):
#     display_letter=""
#     for letter in word:
#         if letter in user_letters:
#             display_letter += letter
#         else:
#             display_letter += "-"
#     return display_letter

# def play():
#     word = get_word()
#     # So'zdagi harflar
#     word_letters = set(word)
#     # Foydalanuvchi kiritgan harflar
#     user_letters = ''
#     print(f"Мен {len(word)} хонали сўз ўйладим. Топа оласизми?")
#     # print(word)
#     while word_letters:
#         print(display(user_letters,word))
#         if user_letters:
#             print(f"Шу вақтгача киритган ҳарфларингиз: {user_letters}")
        
#         letter = input("Ҳарф киритинг: ").upper()
#         if letter in user_letters:
#             print("Бу ҳарфни аввал киритгансиз. Бошқа ҳарф киритинг.")
#             continue        
#         elif letter in word:
#             word_letters.remove(letter)
#             print(f"{letter} ҳарфи тўғри.")
#         else:
#             print("Бундай ҳарф йўқ.")
#         user_letters += letter
#     print(f"Табриклайман! {word} сўзини {len(user_letters)} та уринишда топдингиз.")
  