def triangle(n):
    if n == 1:
        return 1    
    else:
        return triangle(n-1) + n

def power(a,n): # returns a^n, a int, n non-neg int
    if n == 0:
        return 1
    else:
        return power(a,n-1)*a
    
def reverse(st): # returns the reverse of st
    if len(st) == 1 or len(st) == 0:
        return st
    else:
        return reverse(st[1:]) + st[0]

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def anagram(st):
    if st == "":
        return [st]
    else:
        answer = []
        for word in anagram(st[1:]):
            for pos in range(len(word)+1):
                newword = word[:pos] + st[0] + word[pos:]
                if (newword not in answer):
                    answer.append(newword)
        return answer









    


