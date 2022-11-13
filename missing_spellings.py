import random

def missing_spellings(spellings):
    adapted_list = []
    list_length = len(spellings)
    random_removal = random.randint(0, list_length - 1)
    removed_word = spellings[random_removal]
    for x in range(list_length):
        if x == random_removal:
            print("Removing a word...")
        else:
            adapted_list.append(spellings[x])
    random.shuffle(adapted_list)
    points = len(removed_word)
    correct_guess = False
    while not correct_guess:
        print(adapted_list)
        if points == 0:
            print(f"Sorry. You lost! The word was {removed_word}. Keep trying!")
            return points
        else:
            guess = input("Which word has been removed?: ").lower()
            if guess != removed_word.lower():
                points -= 1
                print("No... That's not it. Try again. ")
            else:
                print(f"Great job! You got it! You scored {points} points!")
                correct_guess = True
                return points