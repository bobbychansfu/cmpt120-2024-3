

def multi_tab(r,c):
    maxLength = len(str(r*c))
    for row in range(1,r+1):
        for col in range(1,c+1):
            print(str(row*col).rjust(maxLength), end=" ")
        print()
