import random

# Computer selects a random number between 1 and 10
secret_number = random.randint(1, 10)

guess = 0

print("🎮 Welcome to Number Guessing Game!")
print("Guess a number between 1 and 10")

# Loop until user guesses correctly
while guess != secret_number:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low ❌ Try again")
    elif guess > secret_number:
        print("Too high ❌ Try again")
    else:
        print("🎉 Congratulations! You guessed it right!")
