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
    termcolor.cprint("Start typing a five letter word related to Harry Potter, then click Enter.\n", 'cyan')


playAgain = ""
while playAgain != "q":
    def get_random_word():
        """
        Get random word from words worksheet.
        """
        get_words = SHEET.worksheet("words")
        words = get_words.get_all_values()
        return random.choice(words)
    

    def checkGuess(theAnswer, theGuess): # gets two values
        """
        To check each letter in the user's guess against
        the letters in the chosen random answer.
        """
        clue = ""

        for index, value in enumerate(theGuess):
            if (value.lower() == theAnswer[0][index].lower()):
                clue += colored(value.lower(), 'green')
            elif (value.lower() in theAnswer[0].lower()):
                clue += colored(value.lower(), 'red')
            else:
                clue += "-"
        print(clue)
        return clue == colored(value.lower(), 'green')


def continueGame():
    termcolor.cprint("You have 6 attempts. Start typing a five letter word related to Harry Potter, then click Enter.\n", 'cyan')


startGame()
answer = get_random_word()
print(answer)


attempt = 0
guessed_correctly = False

while attempt <= 6 and not guessed_correctly:
    guess = input().lower()
    print(f"You guessed {colored(guess, 'cyan')}")
    attempt += 1
    guessed_correctly = checkGuess(answer, guess)


if guessed_correctly:
    print(f"Congrats! You got the wordle in {attempt} guesses!")
else:
    print(f"You have used up all your guesses...the correct word is {answer}")

playAgain = input("Want to play again? Type q to exit.")

continueGame()
answer = get_random_word()
