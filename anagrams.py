import random

def anagrams(spellings):    
    random_spelling = random.choice(spellings).upper()
    points = len(random_spelling)
    anagram = []
    for x in random_spelling:
        anagram.append(x)
    random.shuffle(anagram)
    string = ''.join(str(i) for i in anagram)
    print(string)
    correctly_guessed = False
    while not correctly_guessed:
        if points == 0:
            print("Sorry! You lost! Don't worry. We all make mistakes.")
            return points
        else:
            guess = input("What do you think the word is?: ").upper()
            if guess != random_spelling:
                print("Sorry, that's not quite right...")
                points -= 1
            else:
                print(f"That's it! Great job! You scored {points} points")
                correctly_guessed = True
    return points