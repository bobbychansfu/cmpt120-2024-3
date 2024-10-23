def main():
    # open file
    outfile = open('users.txt','a')
    # process
    outfile.write('bob3\n')
    outfile.write('steve3\n')
    outfile.write('jane3')
    # close file
    outfile.close()

main()
