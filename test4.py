from random import*

def start_game():
    print("Unscramble the word")
    print("The words are cat, chicken, or money")
    words = ["cats", "chicken", "money"]
    chosen_word = choice(words)
    letters = list(chosen_word)
    shuffle(letters)
    shuffled = ''.join(letters)
    print ("Scrambled Word:", shuffled)
    trials = 6
    while trials > 0:
        guess= input("Enter Your Guess:")
        if guess == chosen_word:
            print("Correct!")
            return
        else:
            print("Wrong")
    
            trials = trials - 1
            
        if chosen_word == "money":
            print("Hint: A form of currency")
        elif chosen_word == "cat":
            print("Hint: The animal purrs")
        elif chosen_word == "chicken":
            print("Hint: The animal lays eggs")

    if trials == 0:
        print("You Lose. The correct answer was:", chosen_word)
start_game()

