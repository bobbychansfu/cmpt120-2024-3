def main():
    # open file
    infile = open('users.txt','r')
    # process
    line1 = infile.readline().rstrip('\n') # "bob2\n"
    line2 = infile.readline().rstrip('\n')
    line3 = infile.readline().rstrip('\n')
    line4 = infile.readline().rstrip('\n')
    line5 = infile.readline().rstrip('\n')
    line6 = infile.readline().rstrip('\n')
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    print(line6)
    # close file
    infile.close()

main()
