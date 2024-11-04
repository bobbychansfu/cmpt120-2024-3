try:
    filename = input("enter filename: ")
    infile = open(filename,'r')

    c1 = int(infile.readline().rstrip('\n'))
    opn = infile.readline().rstrip('\n')
    c2 = int(infile.readline().rstrip('\n'))

    if (opn == '+'):
        print(c1+c2)
    elif (opn == '-'):
        print(c1-c2)
    elif (opn == '*'):
        print(c1*c2)
    elif (opn == '/'):
        print(c1/c2)
    else:
        print('invalid operation')
except ValueError as er:
    print(er)
except FileNotFoundError:
    print("file not found")
except ZeroDivisionError:
    print("can't divide by 0")
except:
    print("general error")
else:
    print("everything went well!")
finally:
    print("executed no matter what happens")
    
