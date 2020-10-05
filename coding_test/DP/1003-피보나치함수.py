"""
주요 Tip
1. 패턴을 파악하자. --> 0,1호출 숫자도 피보나치수열 패턴을 따르기때문에 쉽게
   풀수 있었다.
"""

k = int(input())

def Fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    if n in cache:
        return cache[n]
    else:
        value = Fib(n-1) + Fib(n-2)
        cache[n] = value
        return value

for _ in range(k):
    cache = {}
    
    n = int(input())
    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    elif n == 2:
        print(1, 1)
    else:    
        Fib(n)
        print(cache[n-1], cache[n])