'''
roots(a,b,c):
parameters a,b,c
find all roots of
ax^2 + bx + c
'''
import math

def roots(a,b,c):
    det = b**2 - 4*a*c
    if det < 0:
        return None
    root1 = (-b + math.sqrt(det)) / (2*a)
    root2 = (-b - math.sqrt(det)) / (2*a)
    return root1,root2

def main():
    a = 6
    b = 1
    c = 4
    rs = roots(a,b,c)
    if rs is None:
        print("no roots")
    else:
        r1 = rs[0]
        r2 = rs[1]
        print(round(r1,2),round(r2,2))

main()
