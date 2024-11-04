infile = open("friends.txt","r")
friends_list = infile.readlines()
print(friends_list)
infile.close()

outfile = open("copy_friends.txt","w")
outfile.writelines(friends_list)
outfile.close()
