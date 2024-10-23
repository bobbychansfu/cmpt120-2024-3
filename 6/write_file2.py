def main():
    # open file
    outfile = open("friends.txt",'a')

    while (True):
        name = input("next friend: ")
        if name == '':
            break
        outfile.write(name + '\n')
        
    print("new friends added to 'friends.txt'")

main()
