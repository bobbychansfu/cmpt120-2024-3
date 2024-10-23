def main():
    # open file
    infile = open('users.txt','r')
    # process
    read_line = infile.read()
    print(read_line)
    # close file
    infile.close()

main()
