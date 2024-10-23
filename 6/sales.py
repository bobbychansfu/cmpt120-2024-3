def main():
    infile = open("sales.txt","r")

    total = 0
    num = infile.readline().rstrip('\n')
    while (num != ''):
        num = float(num)
        total += num
        num = infile.readline().rstrip('\n')
    print(total)
main()
