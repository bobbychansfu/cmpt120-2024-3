import time

# for i in range(5,0,-1):
#     print(i)
#     time.sleep(0.5)

def count_down(n):
    if n < 1:
        print("stop!")
    else:
        print(n)
        time.sleep(0.5)
        count_down(n-1)
        print(n)
        time.sleep(0.5)
        
count_down(5)
