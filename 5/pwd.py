def parse_username_pwd(str_input):
    parsed_str_list = str_input.split()
    return parsed_str_list

def validate(username, password):
    return username == 'bobby' and password == 'BEST54'

def main():
    for i in range(2,-1,-1):
        str_input = input("Enter username and password separated by space: ")
        [username,password] = parse_username_pwd(str_input)
        if(validate(username,password)):
            print("Access Granted!")
            break
        elif(i>0):
            print("Incorrect credentials. You have",i,"attempts left.")
        else:
            print("Account Locked!")

main()
