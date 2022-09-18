from rich.console import Console
from random import choice


welcome_message = "Welcome to Wizard Wordle Game!"
instructions = "You can start guessing with a five letter word."
allowed_guesses = 6

def correct_place(letter):
    return f'[black on green]{letter}[/]'

def correct_letter(letter):
    return f'[black on yellow]{letter}[/]'

def incorrect_letter(letter):
    return f'[black on white]{letter}[/]'

if __name__ == '__main__':
    console = Console()
    chosen_word = choice(word_list)
    console.print(welcome_message)
    console.print(instructions)


