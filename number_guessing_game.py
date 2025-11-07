import random

def number_guessing_game():
    print("=== Welcome To Number Guessing Game ===")
    print("I'm thinking of a number between 1 and 100.")
    
    # Random number generate
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    while not guessed:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                guessed = True
        except ValueError:
            print("Please enter a valid integer.")

# Run the game only once
number_guessing_game()

        