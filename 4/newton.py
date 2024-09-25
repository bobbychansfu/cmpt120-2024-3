a = int(input("a: "))  # sqrt(a)
x = int(input("b: "))  # guess

while(True):
    print(x)
    y = (x + (a/x)) / 2
    if (abs(x-y) < 0.0000001):
        break
    x = y

print(f"{x:.2f}")
