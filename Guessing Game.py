import random

def guessing_game():
    print("Welcome to the guessing game!")

    while True:
        print("\nFirst, let's set the range of numbers.")
        
        # Step 1: Get custom range from the user
        while True:
            try:
                min_range = int(input("Enter the minimum number for the range: "))
                max_range = int(input("Enter the maximum number for the range: "))
                if min_range < max_range:
                    break
                else:
                    print("Minimum number must be less than the maximum number. Try again.")
            except ValueError:
                print("Please enter valid integers for the range.")

        # Step 2: Generate a random number within the user-defined range
        target_number = random.randint(min_range, max_range)
        attempts = 0

        print(f"\nI'm thinking of a number between {min_range} and {max_range}.")

        # Step 3: Start the guessing loop
        while True:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Please enter a valid integer.")
                continue

            attempts += 1

            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
                break

        # Step 4: Ask if the user wants to play again
        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye.")
            break

# Run the game
guessing_game()
