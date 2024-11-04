'''
write_row(n,row_no)
problem:
    ask user for n = [5,13] n must be odd
    if n = 5 print out

    1
  1 3 1
1 3 5 3 1
  1 3 1
    1

'''

def write_row(n,i):
    line_str = ""
    for k in range(1,2*i-1,2):
        line_str += str(k) + " "
    for k in range(2*i-1,0,-2):
        line_str += str(k) + " "
    print((n-2*i+1)*" " + line_str)

def main():
    n = int(input("n: "))
    for k in range(1,n//2 + 2):
        write_row(n,k)

main()
