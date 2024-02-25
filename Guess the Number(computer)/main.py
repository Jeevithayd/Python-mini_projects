def computer_guess_number():
    print("Welcome to the Guess the Number game!")
    print("Think of a number between 1 and 100, and I'll try to guess it.")
    input("Press Enter when you're ready...")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        print("Is your number:", guess)
        response = input("Enter 'l' if my guess is too low, 'h' if it's too high, or 'c' if it's correct: ")

        if response == 'c':
            print("Hooray! I guessed your number in", attempts, "attempts!")
            break
        elif response == 'l':
            low = guess + 1
        elif response == 'h':
            high = guess - 1
        else:
            print("Invalid input. Please enter 'l', 'h', or 'c'.")

        attempts += 1

    else:
        print("Oops! It seems like you didn't play by the rules. Please run the game again and stick to the instructions.")

# Call the function to play the game
computer_guess_number()

