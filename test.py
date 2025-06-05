from random import *

def start_game():
    target = randint(1, 100)  
    guesses = []              
    print("Guess the number from 1-100. You have 7 tries.")

    for attempt in range(1, 8):  
        guess = get_guess(attempt)
        guesses.append(guess)

        if check_guess(guess, target):
            print("Congrats, you guessed correctly!")
            break
    else:
        print("Sorry, you're out of guesses. The number was:", target)

    print("Your guesses were:", guesses)

def get_guess(try_number):
    while True:
        guess = input(f"Try {try_number}: Enter a number: ")
        if guess.isdigit():
            guess = int(guess)
            if 1 <= guess <= 100:
                return guess
            else:
                print("Number must be between 1 and 100.")
        else:
            print("Please enter a valid number.")

def check_guess(guess, number):
    if guess < number:
        print("Too low.")
        return False
    elif guess > number:
        print("Too high.")
        return False
    else:
        return True

start_game()