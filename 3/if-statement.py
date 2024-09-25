'''
ask user for number
print out if it's even

'''

# ask user for number
number = input("enter number: ")

# check if input is a number
if (number.isdigit()):
    number = int(number)
    # check if it's even
    if (number % 2 == 0):
        # print out "even"
        print("even!")
        print("yay!")

print("the end")


