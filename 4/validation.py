'''
 validate the user's input to be between
 1 and 5
'''

inp = int(input("enter value: "))

# validate the user input

while (inp != 1 and inp != 2 and inp != 3 and inp != 4 and inp != 5): # invalid
    inp = int(input("enter value: "))

# inp is [1,5]
print("continue...")
