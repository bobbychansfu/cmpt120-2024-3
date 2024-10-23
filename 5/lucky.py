'''
start = 1
end = 79

output
count sevens = 18
lucky = 11
'''

def get_user_input():
    while (True):
        start = int(input("start: "))
        end = int(input("end: "))
        if (end > start):
            break
    return start,end

def count_7s_and_lucky(start,end):
    count_7 = 0
    div_by_7 = 0

    for i in range(start,end+1):
        count_7 += str(i).count('7')
        if i % 7 == 0:
            div_by_7 += 1
    return count_7,div_by_7

def main():
    start,end = get_user_input()
    c7,db7 = count_7s_and_lucky(start,end)
    print(c7,db7)

main()

    
