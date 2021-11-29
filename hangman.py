import random

lettersGuessed = []

words = open('words.txt',
             'r').read().lower().split()


def chooseWord(words):
    return random.choice(words)


def gameWon(secretWord, lettersGuessed):
    c = 0
    for i in lettersGuessed:
        if i in secretWord:
            c += 1
    if c == len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    s = list()
    for i in secretWord:
        if i in lettersGuessed:
            s.append(i)
    ans = ''
    for i in secretWord:
        if i in s:
            ans += i
        else:
            ans += '_ '
    return ans


def hangman(secretWord):
    print("Welcome to the game, Hangman!")
    print("The word to guess is", len(secretWord), "letters long.")

    global lettersGuessed
    wrongGuesses = 0
    lettersGuessed = []

    while 8 > wrongGuesses:
        if gameWon(secretWord, lettersGuessed):
            print("-------------")
            print("Congratulations, you won!")
            break

        else:
            print("-------------")
            print("You have", 8-wrongGuesses, "guesses left.")

            guess = input("Please guess a letter: ").lower()
            if guess not in "abcdefghijklmnopqrstuvwxyz":
                print("Invalid input")
                continue
            else:

                if(len(guess) != 1):
                    print("Guess only one letter")
                    continue

                if guess in lettersGuessed:
                    print("Oops! You've already guessed that letter:",
                          getGuessedWord(secretWord, lettersGuessed))

                elif guess in secretWord and guess not in lettersGuessed:
                    lettersGuessed.append(guess)
                    print("Correct guess:", getGuessedWord(
                        secretWord, lettersGuessed))

                else:
                    lettersGuessed.append(guess)
                    wrongGuesses += 1
                    print("Oops! That letter is not in my word:",
                          getGuessedWord(secretWord, lettersGuessed))

            if 8 == wrongGuesses:
                print("-------------")
                print("Sorry, you ran out of guesses. The word was", secretWord)
                break

            else:
                continue


secretWord = chooseWord(words).lower()
hangman(secretWord)
