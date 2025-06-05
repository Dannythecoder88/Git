from random import*    

def animal_game():
  print("Guess animal")
  print("You have 3 tries")
  guess = ["cat" ,"dog", "lion"]
  animal = choice(guess)
  tries = 3
  while tries > 0:
    guess = input("Enter your animal:")
    if guess == animal:
        print("Correct, Good Job")
        return
    else:
        print("You are wrong")
        tries = tries -1
    if animal == "lion":
        print("The animal likes to roar")
    elif animal == "cat":
        print("The animal likes to purr")
    elif animal == "dog":
        print("The animal likes to bark")
  if tries == 0:
    print("You lost")

animal_game()
