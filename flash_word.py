import time
import random
from utilities import clear



def choose_difficulty():
    difficulty_chosen = False
    while not difficulty_chosen:
        difficulty = input("Would you like (e)asy, (m)edium or (h)ard?: ").lower()
        if difficulty in ["e", "m", "h"]:
            difficulty_chosen = True
            return difficulty

def guess_word(difficulty, random_spelling):
    clear()
    print(random_spelling)
    if difficulty == "e":
        time.sleep(1.5)
    elif difficulty == "m":
        time.sleep(1)
    else:
        time.sleep(0.5)
    clear()
    guess = input("What was the word?: ").upper()
    return guess


def flash_word(spellings):
    random_spelling = random.choice(spellings).upper()
    potential_points = len(random_spelling)
    difficulty = choose_difficulty()
    guess_correct = False
    while not guess_correct:
        if potential_points == 0:
            print("Sorry! You lost! Don't worry. Keep going and you'll get it!")
            return potential_points
        else:
            guess = guess_word(difficulty, random_spelling)
            if guess == random_spelling:
                if difficulty == "e":
                    points = potential_points / 2
                elif difficulty == "m":
                    points = potential_points
                else:
                    points = potential_points * 2
                print(f"That's right! You got {int(points)} points!")
                guess_correct = True
                return points
            else:
                print("Sorry. That's not quite right.")
                potential_points -= 1

