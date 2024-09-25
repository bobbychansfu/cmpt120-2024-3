'''
 user for input n and then
 reads n numbers, adding only
 the positive numbers
'''

n = int(input("n: "))

positive_sum = 0
count = 0

while (count < n):
    count = count + 1

    x = int(input("enter next number: "))

    # continue?
    if (x < 0):
        continue
    
    positive_sum = positive_sum + x

print(positive_sum)
