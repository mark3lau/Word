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


def welcome():
    """
    Print coloured text with welcome message and
    instructions for the user to play the game.
    """
    termcolor.cprint("Welcome to the Harry Potter Wordle Game!\n", 'cyan')
    termcolor.cprint("You have 6 attempts. If the letter shows up green, it's correct and in the right position.", 'cyan') 
    termcolor.cprint("If it's red, the letter is in the word but not in the right position. If it shows up as a dash, the letter is not in the word.\n", 'cyan')
    termcolor.cprint("Think of a five letter word related to Harry Potter...\n", 'cyan')


def get_random_word():
    """
    Get a random word from words worksheet.
    """
    get_words = SHEET.worksheet('words')
    words = get_words.get_all_values()
    return random.choice(words)
    

def check_guess(the_answer, the_guess):
    """
    To check each letter in the user's guess against
    the letters in the chosen random answer.
    Display different colours to indicate right 
    and wrong answers.
    """
    clue = ''

    for index, value in enumerate(the_guess):
        if (value.lower() == the_answer[index].lower()):
            clue += colored(value.lower(), 'green')
        elif (value.lower() in the_answer.lower()):
            clue += colored(value.lower(), 'red')
        else:
            clue += '-'
    print(clue)
    return the_guess == the_answer.lower()


def play_game():
    """
    Function to run the game until the user gets
    the correct answer, or uses up all six attempts.
    Check the user's input is 5 letters otherwise
    display error message. 
    Display congratulations message and commiserations 
    messages if guessed correctly or not.
    Option for user to exit game.
    """
    welcome()
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
        guessed_correctly = check_guess(answer, guess)
  
    if guessed_correctly:
        print(f'Congrats! You got the wordle in {attempt} guesses!')
    else:
        print(f'You have used up all your guesses...the correct word is {answer}')

    play_again = input("Press Enter to play again! Or type 'mischief managed' to exit...").lower()

    if play_again != 'mischief managed':
        play_game()
    else:
        print('Thanks for playing the Harry Potter Wordle game.')


if __name__ == '__main__':
    play_game()