'''
  collect user integer input and
  compare it with a secret number
  between 1,100.
  The program will output the relativity
'''
import random

# define the secret number
SECRET = random.randint(1,100)      # randomized number

# collect user input
guess = int(input("guess an integer between [1,100]: "))

# test relativitiy of secret number
# print out result to user

if (guess > SECRET):                # guess < SECRET
    print("guess is too large.")
    print()
elif (guess < SECRET):              # guess < SECRET
    print("guess is too small.")
    print()
else:                               # guess == SECRET
    print("the guess is correct!!!")
    print()

    # keep playing until secret has been guessed - topic 4
    
print("thank you for playing! The SECRET is", SECRET)
