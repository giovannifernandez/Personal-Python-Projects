# Import the random module to generate random numbers
import random

# Define the main function of the game
def guess_the_number():
    # Generate a random number between 1 and 100 and store it in number_to_guess
    number_to_guess = random.randint(1, 100)
    guess = None

    # Start a loop that continues until the player guesses the number
    while guess != number_to_guess:
        # Ask the player for their guess and convert it to an integer
        guess = int(input("Guess a number between 1 and 100: "))

        # Give feedback based on the player's guess
        if guess < number_to_guess:
            print("Higher...")
        elif guess > number_to_guess:
            print("Lower...")
        else:
            # The player guessed correctly, so congratulate them and exit the loop
            print(f"Congratulations! You guessed the number {number_to_guess} correctly.")

# Check if this script is the main program and not being imported by another module
if __name__ == "__main__":
    # If it is the main program, call the guess_the_number function to start the game
    guess_the_number()
