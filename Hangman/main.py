import random

def choose_word():
    word_list = ["antman", "ironman", "captainamerica", "thor", "hulk", "loki"]
    return random.choice(word_list)

def hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("Guess the word!")

    while True:
        displayed_word = ""
        for letter in word:
            if letter in guessed_letters:
                displayed_word += letter
            else:
                displayed_word += "_"

        print(displayed_word)

        if displayed_word == word:
            print("Congratulations! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            incorrect_guesses += 1
            print("Incorrect guess.")
            if incorrect_guesses == max_incorrect_guesses:
                print("Sorry, you're out of guesses! The word was:", word)
                break
        else:
            print("Correct guess!")

hangman()

