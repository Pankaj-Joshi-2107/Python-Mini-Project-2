import random

num = random.randint(1, 10)
tries = 0

while True:
    try:
        guess = int(input("Please guess a number between 1 and 10: "))
        tries += 1

        if guess == num:
            print(f"You are right! You guessed the number in {tries} tries.")
            break
        elif guess > num:
            print("Go a little lower.")
        elif guess < num:
            print("Go a little higher.")
    except ValueError:
        print("Invalid input! Please enter an integer between 1 and 10.")
