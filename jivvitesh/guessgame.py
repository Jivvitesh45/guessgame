import random

def guess_the_number():
    print("Welcome to 'Guess the Number' game!")
    print("I have selected a number between 1 and 100. Try to guess it.")

    number_to_guess = random.randint(1, 100)

    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempts} attempts.")

guess_the_number()
