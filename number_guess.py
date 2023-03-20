import random

logo = """
                             888                             
                             888                             
                             888                             
88888b. 888  88888888b.d88b. 88888b.  .d88b. 888d888.d8888b  
888 "88b888  888888 "888 "88b888 "88bd8P  Y8b888P"  88K      
888  888888  888888  888  888888  88888888888888    "Y8888b. 
888  888Y88b 888888  888  888888 d88PY8b.    888         X88 
888  888 "Y88888888  888  88888888P"  "Y8888 888     88888P' 
                                                             
"""

print(logo)

EASY = 10
HARD = 5


def set_difficulty():
    difficulty = input("Choose a difficutly. Type 'easy' or 'hard': ")
    if difficulty == "hard":
        return HARD
    else:
        return EASY 
    
def check_guess(guess, random_num, turns):
    if guess > random_num:
        print("Too high.")
        turns -= 1
        return turns
    elif guess < random_num:
        print("Too low.")
        turns -= 1
        return turns
    elif guess == random_num:
        print(f"You got it! The answer is {random_num}")
  
    
    
def game():  
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100")
    random_num = random.randint(1,100)    
    # Testing Code:
    print(f"pssst, the number is {random_num}")
    turns = set_difficulty() 
    
    
    guess = 0
    while guess != random_num:
        print(f"You have {turns} turns remaining, to geuss the number.")
        guess = int(input("Make a guess: "))
        turns = check_guess(guess, random_num, turns)
        if turns == 0:
            print("You ran out of guesses. You lose. Bummer :(")
            return
        

game()

    



