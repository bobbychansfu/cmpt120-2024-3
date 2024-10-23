number = 6
PI = 3.14

def area_circle(radius):
    a = PI * radius**2
    print(a)

def change():
    global number
    number = 2
    print("this is the scope of change: ",number)
    return 

def main():
    change()
    print("this is the scope of main: ",number)
    area_circle(9)

main()
