from JES import *
from math import*
from random import*

def fruit_game():
    guess = [apple,pear,banana]
    word = random.choice(words)
    tries = 6
print("Guess fruit")
print("You have 3 tries:")

while tries >0:
    guess = input("Enter your frut")
if guess == word:
    print("Correct, Good Job")
else:
    print("You are wrong")
    tries = tries -1

if tries == 0:
    print("You lost")

