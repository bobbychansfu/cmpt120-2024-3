'''
  takes user's full name input via terminal
  print out their first and last name separately
  i.e. 'Bobby C Chan' is entered, display
  > first name: Bobby
  > last name: Chan
  assume that last space indicastes the separation
'''

# 1. collect input from user
fullname = input("Enter your full name: ")

# 2. find the index of the 'space'
index = fullname.rfind(" ")      # find index
first_name = fullname[:index]    # split into first name variables
last_name = fullname[index+1:]   # splait last name variable

# 3. display user's first/last name
outputString = ("> first name: " + first_name + "\n"
                "> last name:  " + last_name)
print(outputString)





...  # inline - comments on one line of code
...

