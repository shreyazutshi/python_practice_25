def play_game():
    n = random.randint(0, 100)
    i = 1

    print("Welcome to the Number Guessing Game!")
    print("Guess the number between 0 and 100. You have 9 attempts.\n")

    while i <= 9:
        try:
            user_input = int(input(f"Attempt {i}: Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue

        if user_input > n:
            print(f"Too high! {9 - i} guesses left.\n")
        elif user_input < n:
            print(f"Too low! {9 - i} guesses left.\n")
        else:
            print(f"Yay! You guessed the number correctly in {i} attempts!\n")
            break

        i += 1

    else:
        print(f"You've used all your guesses. The correct number was {n}.\n")

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
