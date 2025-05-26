'''
  display student's lettergrade based
  on percentage

  > 85 = A
  > 75 = B
  > 65 = C
  > 55 = D
  <= 55 = F
'''

# constants
A_CUTOFF = 85
B_CUTOFF = 75
C_CUTOFF = 65
D_CUTOFF = 55

# collect user's percentage as a float
percent = float(input("enter percentage: "))

# determine the lettergrade - method 1
lettergrade = ""
if (percent > A_CUTOFF):
    lettergrade = "A"
elif (percent > B_CUTOFF):
    lettergrade = "B"
elif (percent > C_CUTOFF):
    lettergrade = "C"
elif (percent > D_CUTOFF):
    lettergrade = "D"
else:
    lettergrade = "F"

# determine the lettergrade - method 2
if (percent <= 55):
    lettergrade = "F"
else:                   # percent > 55
    if (percent <= 65):
        lettergrade = "D"
    else:
        if (percent <= 75):
            lettergrade = "C"
        else:
            if (percent <=85):
                lettergrade = "B"
            else:
                lettergrade = "A"


# printout the lettergrade
print("your lettergrade:", lettergrade)
