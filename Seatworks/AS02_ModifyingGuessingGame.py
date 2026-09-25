import random

def play_game(best_score):
    print("\n--- NUMBER GUESSING GAME ---")
    print()
    
    # 1. Let the player choose the number range
    lower = int(input("Enter lower bound: "))
    upper = int(input("Enter upper bound: "))
    print()
    
    secret = random.randint(lower, upper)
    attempts = 0
    max_attempts = 7  # 2. Limit to 7 attempts
    guessed = False

    print(f"I'm thinking of a number between {lower} and {upper}.")
    print(f"You have {max_attempts} attempts.")
    print("*" * 20)
    print()

    while attempts < max_attempts and not guessed:
        user_input = input("Enter your guess: ")
        guess = int(user_input)
        attempts += 1

        if guess < secret:
            print("Too low! Try again.\n")
        elif guess > secret:
            print("Too high! Try again.\n")
        else:
            guessed = True
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            
            # 3. Track best score
            if best_score == 0 or attempts < best_score:
                best_score = attempts
                print("New Best Score!")
            print()

    # If lost after 7 attempts
    if not guessed:
        print(f"Game Over! You ran out of attempts. The number was {secret}.")
        print()

    return best_score

def main():
    best_score = 0
    keep_playing = True

    while keep_playing:
        best_score = play_game(best_score)

        if best_score > 0:
            print(f"Best Score so far: {best_score} attempts")
            print()

        # 4. Option to play again
        choice = input("Do you want to play again? (yes/no): ")
        if choice == 'no' or choice == 'NO':
            keep_playing = False
            print("Thanks for playing! Goodbye.")
            print()

main()