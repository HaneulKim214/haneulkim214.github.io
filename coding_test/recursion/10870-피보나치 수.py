"""
주요 Tip:
1. 없다.

Q: Where is Fibonacci used...?
"""

# Top-down
n = int(input())

def Fib(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return Fib(n-1) + Fib(n-2)    


# Bottom-up
def Fib(n):
    d = [0]*n+1
    d[0] = 0
    d[1] = 1

    for i in range(2, n):
        d[i] = d[i-1] + d[i-2]
    return d[n-1] + d[n-2]
