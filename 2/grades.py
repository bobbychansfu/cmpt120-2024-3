'''
Given the cutoffs:
< 50% - F
< 60% - D
< 70% - C
< 80% - B
>= 80 - A
ask user for a percentage,
output the lettergrade
'''

A_CUTOFF = 80
B_CUTOFF = 70
C_CUTOFF = 60
D_CUTOFF = 50

percent = float(input("enter percent: "))
'''
if (percent >= A_CUTOFF):
    print("A")
elif (percent >= B_CUTOFF):
    print("B")
elif (percent >= C_CUTOFF):
    print("C")
elif (percent >= D_CUTOFF):
    print("D")
else:
    print("F")
'''
if (percent < D_CUTOFF):
    print("F")
else: # percent >= 50
    if (percent <C_CUTOFF):
        print("D")
    else: # percent >= 60
        if (percent < B_CUTOFF):
            print("C")
        else: # percent >= 70
            if (percent < A_CUTOFF):
                print("B")
            else:
                print("A")





                
