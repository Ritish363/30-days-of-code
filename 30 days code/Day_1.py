import random

print("Welcome to Number Guessing Game!")

# Generate random number
number = random.randint(1, 100)

attempts = 0

while True:
    try:
        guess = int(input("Enter your guess (1-100): "))
        attempts += 1

        if guess < number:
            print("Too low ⬇️")
        elif guess > number:
            print("Too high ⬆️")
        else:
            print(f"Correct! 🎉 You guessed it in {attempts} attempts.")
            break

    except ValueError:
        print("Please enter a valid number!")
