'''
guessing game that asks the user
for a guess between 1 and 100,
then prints out whether guess
is correct, too high, or too low,
*update*
then loops until the correct guess is
obtained
'''
import random

MAX_GUESSES = 7
SECRET = random.randint(1,100)

guess = None  # Initialize guess variable
for _ in range(MAX_GUESSES):
    guess = int(input("enter guess [1,100]: "))

    if (guess == SECRET):
        print("CONGRATS ... you got it!")
        break
    elif (guess > SECRET):
        print("guess is too high")
    else:
        print("guess is too low")

print("secret number",SECRET)
