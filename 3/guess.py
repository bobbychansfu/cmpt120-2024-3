'''
guessing game that asks the user
for a guess between 1 and 100,
then prints out whether guess
is correct, too high, or too low
'''
import random

SECRET = random.randint(1,100)
guess = int(input("enter guess [1,100]: "))

if (guess == SECRET):
    print("you got it!")
elif (guess > SECRET):
    print("guess is too high")
else:
    print("guess is too low")

print("secret number",SECRET)
