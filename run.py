import gspread
from google.oauth2.service_account import Credentials
import random
import sys
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


def game():
    print("Welcome to the Harry Potter Wordle Game!\n")
    print("Start typing a five letter word related to Harry Potter, then click Enter.\n")

def get_random_word():
    """
    Get random word from words worksheet.
    """
    get_words = SHEET.worksheet("words")
    words = get_words.get_all_values()
    return random.choice(words)
   

game()
word = get_random_word()


for attempt in range(1, 7):
    guess = input().lower()

    for i in range(min(len(guess), 5)):
        if guess[i] == word[i]:
            print(colored(guess[i], 'green'), end="")
        elif guess[i] in word:
            print(colored(guess[i], 'yellow'), end="")
        else:
            print(guess[i], end="")

    if guess == word:
        print(f"Congrats! You got the wordle in {attempt}")
        break