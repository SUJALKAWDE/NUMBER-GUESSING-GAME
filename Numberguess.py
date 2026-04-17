import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 50.")
    
    # Generate random number
    secret_number = random.randint(1, 50)
    
    # Number of attempts allowed
    attempts = 7

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}/{attempts} - Enter your guess: "))
        
        if guess < secret_number:
            print("Too low! 📉")
        elif guess > secret_number:
            print("Too high! 📈")
        else:
            print(f"🎉 Congratulations! You guessed the number in {attempt} attempts.")
            break
    else:
        print(f"❌ Sorry, you’ve used all attempts. The number was {secret_number}.")

# Run the game
number_guessing_game()


