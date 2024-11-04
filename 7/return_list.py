def alter(lst):
    lst[0] = 10
    return

def main():
    alst = [1,2,3,4]
    alter(alst[:])
    print(*alst)

main()
