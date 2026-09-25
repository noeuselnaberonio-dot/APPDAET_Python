import random

def play_game():
    secret = random.randint(1, 100)
    attempts = 0
    guessed = False

    # your code here
    print()
    print("Welcome to the Number Guessing Game!")
    print()
    print("I'm thinking of a number between 1 and 100.\n")
    print("Can you guess what it is?")
    print()
    print("*" * 20)
    print()

    while not guessed:

        #your code here
        user_input = input("Enter your guess (or type 'exit' to quit): ")

        if user_input == 'exit' or user_input == 'Exit':
            print("Thanks for playing! Goodbye.")
            break

        guess = int(user_input)
        attempts += 1

        if guess < secret:
            print("Too low! Try again.\n")
        elif guess > secret:
            print("Too high! Try again.\n")
        else:
            guessed = True
            print(f"Congratulations! You've guessed the number {secret} in {attempts} attempts.")
            print()

play_game()