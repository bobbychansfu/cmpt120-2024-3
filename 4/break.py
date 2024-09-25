'''
 add all user inputs
 until the user enters a negative number
'''

total = 0

# loop

num = 10000
while (num >= 0):
    num = int(input("plz enter num: "))

    # break?
    if (num < 0):
        break
    
    total = total + num

print(total)
