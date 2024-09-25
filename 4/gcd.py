'''
 find gcd of a and b
'''

a = int(input("a: "))
b = int(input("b: "))

while (True):
    r = a % b
    if (r == 0):
        break
    a = b
    b = r

print(b)
