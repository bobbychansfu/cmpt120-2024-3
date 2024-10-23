'''
 given r,c (ints)
 print out a rxc
 multiplication table
 r = 2,  c = 3

 1 2 3
 2 4 6
'''

# grabbing r,c
inpt = input("enter r,c separated by space: ")
inp_list = inpt.split()
r = int(inp_list[0])
c = int(inp_list[1])



# print out multi-table

maxLength = len(str(r*c))
for row in range(1,r+1):
    for col in range(1,c+1):
        print(str(row*col).rjust(maxLength), end=" ")
    print()
