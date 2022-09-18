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
    get_words = SHEET.worksheet("words")
    words = get_words.get_all_values()
    random_word = (random.choice(words))
    return random_word

game()
word = get_random_word()

