import gspread
from google.oauth2.service_account import Credentials
import random
import termcolor
from termcolor import colored

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('harry_potter_wordle')


def startGame():
    termcolor.cprint("Welcome to the Harry Potter Wordle Game!\n", 'cyan')
    termcolor.cprint("You have 6 attempts. If the letter shows up green, it's correct and in the right position. If it's red, the letter is in the word but not in the right position. If it shows up as a dash, the letter is not in the word.\n", 'cyan')
    termcolor.cprint("Think of a five letter word related to Harry Potter...\n", 'cyan')


def get_random_word():
    """
    Get random word from words worksheet.
    """
    get_words = SHEET.worksheet("words")
    words = get_words.get_all_values()
    return random.choice(words)
    

def checkGuess(theAnswer, theGuess):
    """
    To check each letter in the user's guess against
    the letters in the chosen random answer.
    """
    clue = ""

    for index, value in enumerate(theGuess):
        if (value.lower() == theAnswer[index].lower()):
            clue += colored(value.lower(), 'green')
        elif (value.lower() in theAnswer.lower()):
            clue += colored(value.lower(), 'red')
        else:
            clue += "-"
    print(clue)
    return theGuess == theAnswer.lower()


def playGame():
    startGame()
    answer = get_random_word()[0]
    print(answer)

    attempt = 0
    guessed_correctly = False

    while attempt <= 6 and not guessed_correctly:
        guess = input('Enter your guess here: ').lower()
        if len(guess) != len(answer):
            print('You need to type a 5 letter word, try again')
            continue
        print(f"You guessed {colored(guess, 'cyan')}")
        attempt += 1
        guessed_correctly = checkGuess(answer, guess)
  
    if guessed_correctly:
        print(f"Congrats! You got the wordle in {attempt} guesses!")
    else:
        print(f"You have used up all your guesses...the correct word is {answer}")

    playAgain = input("Want to play again? If not type 'mischief managed' to exit.").lower()

    if playAgain != "mischief managed":
        playGame()
    else:
        print("Thanks for playing the Harry Potter Wordle game.")


if __name__ == '__main__':
    playGame()