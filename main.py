import random
def play_game():
    print("\n" + "=" * 45)
    print("        NUMBER GUESSING GAME")
    print("=" * 45)
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    print(f"I picked a number between 1 and 100. You have {max_attempts} attempts!\n")

    while attempts < max_attempts:
        try:
            guess = int(input(f"[{attempts + 1}/{max_attempts}] Your guess: "))
        except ValueError:
            print("Please enter a valid integer!\n")
            continue

        attempts += 1
        if guess == secret_number:
            print(f"\nCongratulations! You guessed the number in {attempts} attempts! (Number: {secret_number})")
            break
        elif guess > secret_number:
            print("Guess a SMALLER number.")
        else:
            print("Guess a LARGER number.")
    else:
        print(f"\nOut of attempts! The number was: {secret_number}")
def main():
    while True:
        play_game()
        replay = input("\nDo you want to play again? (y/n): ").strip().lower()
        if replay != 'y':
            print("\nThanks for playing! Goodbye.")
            break
if __name__ == "__main__":
    main()