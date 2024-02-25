import random

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    
    secret_number = random.randint(1, 100)
    
    attempts = 0
    guessed = False
  
    while not guessed:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess == secret_number:
            print("Congratulations! You guessed the number in", attempts, "attempts!")
            guessed = True
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# Call the function to play the game
guess_the_number()
