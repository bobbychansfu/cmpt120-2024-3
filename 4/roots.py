'''
 roots
 collect 2 integers a,b
 print all square roots
 btween a and b
 i.e. a = 2 b = 5
 sqrt(2)
 sqrt(3)
 ...
'''
import math

# collect inputs a,b
a = int(input("a: "))
b = int(input("b: "))

x = 1
if (a > b):
    x = -1

# cycle thru values from a to b
for val in range(a,b+x,x):
    # print out sq(value)
    print(round(math.sqrt(val),2))
