from JES import *
from math import*
from random import*

def start_game():
    Correct = random.randit(0,100)
    guesses = {}

    for attempt in range ((1,8)):
        get_guess(attempt)
        guesses.append(guess)
    if right_guess(guess, target_):
        print("Congrats, you guessed correctly")
    else:
        print("Sorry, you are all out of guesses")

def get_guess(try_number):
    guess = input(f"Try {try_number}: Enter a number: ")
    if guess.isdigit():
        guess = int(guess)
        if 1 <= guess <= 100:
            return guess
        else:
            print("Number must be between 1 and 100.")

def check_guess(guess, number):
    if guess < number:
        print("Too low.")
        return False
    elif guess > number:
        print("Too high.")
        return False
    else:
        return True
