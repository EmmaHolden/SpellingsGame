import random
from utilities import clear

def get_random_spelling(spellings):
    mystery_spelling = random.choice(spellings).upper()
    return mystery_spelling

def create_display(chosen_word):
    display = []
    word_length = len(chosen_word)
    for _ in range(word_length):
        display += "_"
    print(display)
    return display

def points_available(display):
    points_available = 0
    for x in display:
        if x == "_":
            points_available += 1
    if points_available == 0:
        print("Sorry. You lost! Never mind. Practice makes perfect!")
    else:
        print(f"There are {points_available} points available for this word.")
    return points_available

def ready_to_guess():
    answered_question = False
    while not answered_question:
        want_to_guess = input("Do you think you know the word? Type 'yes' or 'no': ").lower()
        if want_to_guess in ["yes", "y", "no", "n"]:
            answered_question = True
            clear()
            return want_to_guess

def make_a_guess(chosen_word):
    guess = input("What do you think the word is?: ").upper()
    return guess == chosen_word

def reveal_a_letter(chosen_word, display):
    letters_left_to_see = []
    for x in range(len(display)):
        if display[x] == "_":
            letters_left_to_see.append(x)
    index_of_letter = random.choice(letters_left_to_see)
    display[index_of_letter] = chosen_word[index_of_letter]
    print(display)
    return display

def missing_letters(spellings):
    chosen_word = get_random_spelling(spellings)
    display = create_display(chosen_word)
    end_of_game = False
    while not end_of_game:
        points = points_available(display)
        if points == 0:
            end_of_game = True
        else:
            want_to_guess = ready_to_guess()
            if want_to_guess == "yes" or want_to_guess == "y":
                guess = make_a_guess(chosen_word)
                if guess:
                    print(f"Great job! You got it right! You scored {points} points!")
                    end_of_game = True
                    return points
                else:
                    print("Sorry! That's wrong!")
                    reveal_a_letter(chosen_word, display)
            else:
                print("Okay. Let's reveal a letter.")
                reveal_a_letter(chosen_word, display)
    return points