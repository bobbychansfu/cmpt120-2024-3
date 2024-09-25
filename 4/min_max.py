'''
repeatly ask user for integers
report the min and max of the integers
'''

# problem!
inp = int(input("next number (enter 'exit' to stop): "))

mini = inp
maxi = inp

while (inp != 'exit'):
    number = int(inp)
    if (number < mini):
        mini = number
    elif (number > maxi):
        maxi = number
    inp = input("next number (enter 'exit' to stop): ")

print("max:", maxi, "min:", mini)
