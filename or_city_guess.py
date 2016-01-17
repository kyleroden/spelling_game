import random
import os
import sys

#guess the Oregon City

cities = [
'baker',
'burns',
'pendleton',
'eugene',
'springfield',
'newport',
'portland',
'salem',
'corvallis',
'bend',
'astoria'
]

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def draw(bad_guesses, good_guesses, selected_city):
    clear()

    print("Strikes: {}/7".format(len(bad_guesses)))
    print("")

    for letter in bad_guesses:
        print(letter, end=' ')
    print('\n\n')

    for letter in selected_city:
        if letter in good_guesses:
            print(letter, end="")
        else:
            print("_", end='')
    print('')

def get_guess(bad_guesses, good_guesses):
    while True:
        guess_letter = input("Enter a letter -> ").lower()

        if len(guess_letter) != 1:
            print('You can only enter one letter at a time.')
        elif guess_letter in good_guesses or guess_letter in bad_guesses:
            print("You've already guessed that letter.")
        elif guess_letter.isalpha() == False:
            print("You can only guess letters.")
        else:
            return guess_letter

def play(done):
    clear()
    selected_city = random.choice(cities)
    bad_guesses = []
    good_guesses = []

    while True:
        draw(bad_guesses, good_guesses, selected_city)
        guess = get_guess(bad_guesses, good_guesses)

        if guess in selected_city:
            good_guesses.append(guess)
            found = True
            for letter in selected_city:
                if letter not in good_guesses:
                    found = False
            if found:
                print("You win!")
                print("The secret city was {}".format(selected_city))
                done = True
        else:
            bad_guesses.append(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses, good_guesses, selected_city)
                print("You lost.")
                print("The secret city was {}".format(selected_city))
                done = True
        if done:
            play_again = input("Play again? Enter y/n. ").lower()
            if play_again != 'n':
                return play(done=False)
            else:
                sys.exit()

def welcome():
    start = input("Press enter/return to start or Q to exit.").lower()
    if start == 'q':
        print("Farewell.")
        sys.exit()
    else:
        return True
print("Welcome to the Oregon Cities Game. Guess the correct Oregon city, one letter at a time. Ignore capitalization.")

done = False

while True:
    clear()
    welcome()
    play(done)
