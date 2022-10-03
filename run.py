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
    print("You have 6 attempts. Start typing a five letter word related to Harry Potter, then click Enter.\n")

def get_random_word():
    """
    Get random word from words worksheet.
    """
    get_words = SHEET.worksheet("words")
    words = get_words.get_all_values()
    return random.choice(words)
   

def check_guess(answer, guess):
    position = 0
    for letter in guess:
        if letter == answer[position]:
            print(colored(guess[letter]), 'green')
        elif letter in answer:
            print(colored(guess[letter]), 'yellow')
        else:
            print(guess[letter])
        position += 1
    print(guess)
    

game()
answer = get_random_word()
print(answer)

attempt = 0
guessed_correctly = False

while attempt < 6 and not guessed_correctly:
    guess = input().lower()
    print(f"You guessed {guess}")
    attempt += 1

    guessed_correctly = check_guess(answer, guess)

if guessed_correctly:
    print(f"Congrats! You got the wordle in {attempt} guesses!")
else:
    print(f"You have used up all your guesses...the correct word is {answer}")


# for attempt in range(7):
#     guess = input().lower()

#     for i in range(4):
#         if guess[i] == answer[i]:
#             print(colored(guess[i], 'green'), end="")
#         # elif guess[i] in word:
#         #     print(colored(guess[i], 'yellow'), end="")
#         # else:
#         #     print(guess[i], end="")

#     if guess == computer:
#         print(f"Congrats! You got the wordle in {attempt}")
#         break


# for i in range(min(len(guess), 4)):