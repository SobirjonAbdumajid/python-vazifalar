import random

wordList = [
    "wares",
    "soup",
    "mount"
]

def get_word():
    randomIndex = random.randint(0, len(wordList) - 1)
    return wordList[randomIndex].upper()

def play(word):
    wordCompletion = "_" * len(word)
    guessed = False
    guessedLetters = []
    guessedWords = []
    tries = 6

    print("Let's play Hangman!")
    display_hangman(tries)
    print(wordCompletion)
    print()

    while not guessed and tries > 0:
        guess = input().upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessedLetters:
                print(f"You already guessed the letter {guess}")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessedLetters.append(guess)
            else:
                print(f"Good job, {guess} is in the word!")
                guessedLetters.append(guess)
                wordArray = list(wordCompletion)
                for i in range(len(word)):
                    if word[i] == guess:
                        wordArray[i] = guess
                wordCompletion = "".join(wordArray)

                if "_" not in wordCompletion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessedWords:
                print(f"You already guessed the word {guess}")
            elif guess != word:
                print(f"{guess} is not the word.")
                tries -= 1
                guessedWords.append(guess)
            else:
                guessed = True
                wordCompletion = word
        else:
            print("Not a valid guess.")

        display_hangman(tries)
        print(wordCompletion)
        print()

    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print(f"Sorry, you ran out of tries. The word was {word}. Maybe next time!")

def display_hangman(tries):
    stages = [
        # final state: head, torso, both arms, and both legs
        """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
            """,
        # head, torso, both arms, and one leg
        """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / 
               -
            """,
        # head, torso, and both arms
        """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |      
               -
            """,
        # head, torso, and one arm
        """
               --------
               |      |
               |      O
               |     \\|
               |      |
               |     
               -
            """,
        # head and torso
        """
               --------
               |      |
               |      O
               |      |
               |      |
               |     
               -
            """,
        # head
        """
               --------
               |      |
               |      O
               |    
               |      
               |     
               -
            """,
        # initial empty state
        """
               --------
               |      |
               |      
               |    
               |      
               |     
               -
            """
    ]

    print(stages[tries])

def main():
    word = get_word()
    print(word)
    play(word)
    while True:
        answer = input("Play Again? (Y/N) ").upper()
        if answer == "Y":
            word = get_word()
            play(word)
        elif answer == "N":
            break
        else:
            print("Please give correct answer")

if __name__ == "__main__":
    main()