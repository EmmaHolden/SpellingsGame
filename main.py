
from missing_letters import *
from missing_spellings import *
from flash_word import *
from anagrams import *
from utilities import clear
import os

spelling_games = ["Missing Letters"]

def ready():
    print("Welcome to your spelling test practice.")
    print("First, you're going to enter your weekly spellings. Be really careful to enter them correctly.")
    print("It might be a good idea to ask an adult to help you with this bit.")
    ready_to_start = False
    while not ready_to_start:
        spellings = []
        number_of_spellings = enter_number()
        spellings_entered = enter_spellings(number_of_spellings, spellings)
        spellings_checked = check_spellings(spellings)
        if spellings_checked:
            print("Let's play a game!")
            print(spellings)
            ready_to_start = True
            return spellings


def enter_number():
    number_entered = False
    while not number_entered:
        raw_number_of_spellings = (input("How many spellings do you have to learn this week?: "))
        if raw_number_of_spellings.isdigit():
            number_of_spellings = int(raw_number_of_spellings)
            check_number = False
            while not check_number:
                check = input(f"Okay. So you have {number_of_spellings} this week. Is that right?: ").lower()
                if check == "yes" or check == "y":
                    return number_of_spellings
                elif check == "no" or check == "n":
                    check_number = True
        else:
            print("Please enter a number: ")


def enter_spellings(number_of_spellings, spellings):
    spellings_entered = False
    while not spellings_entered:
        for x in range(1, number_of_spellings + 1):
            spelling = input(f"Please type spelling number {x}: ")
            spellings.append(spelling)
        return spellings


def check_spellings(spellings):
    spellings_checked = False
    while not spellings_checked:
        checking = input(f"So your spellings are {spellings}. Is this correct?: ")
        if checking == "yes" or checking == "y":
            spellings_entered = True
            return spellings_entered
        elif checking == "no" or checking == "n":
            spellings_entered = False
            return spellings_entered
        else:
            spellings_checked = False

def play_again(points):
    play_again = input(f"So far you have {points} points! Would you like to play another game?: ").lower()
    if play_again == "yes" or play_again == "y":
        game_over = False
        clear()
    else:
        game_over = True
    return game_over

clear()
spellings = ready()
clear()
points = 0
game_over = False
while not game_over:
    game_choice = input("Which game would you like to play?\nA - Missing Letters\nB - Missing Spellings\nC - Anagrams\n"
                        "D - Flash Word\n").upper()
    if game_choice == "A":
        points += missing_letters(spellings)
        game_over = play_again(points)
    elif game_choice == "B":
        points += missing_spellings(spellings)
        game_over = play_again(points)
    elif game_choice == "C":
        points += anagrams(spellings)
        game_over = play_again(points)
    elif game_choice == "D":
        points += int(flash_word(spellings))
        game_over = play_again(points)
if game_over:
    print(f"You finished with {points} points! Great job!")



