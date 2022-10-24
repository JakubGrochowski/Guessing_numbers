import random
import time

print("Hi! Welcome to the guessing game. I'm going to pic a number between 1 to 100")
time.sleep(3)
print("Picking a number ...")
time.sleep(2)
guess_number = int(input("What is your guess?: "))

correct_number = random.randint(1, 100)
guess_count = 1

while guess_number != correct_number:
    time.sleep(1)
    guess_count += 1
    if guess_number < correct_number:
        guess_number = int(input("Oops it's not right number, you need to guess higher - try again: "))
    else:
        guess_number = int(input("Oops it's not right number, you need to guess lower - try again: "))

print(f"Congrats! The right number was {correct_number}. It took you {guess_count} guesses")
