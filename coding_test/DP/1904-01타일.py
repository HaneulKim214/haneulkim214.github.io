"""
점화식(recurrence formula)의 값을 특정 상수로 나눈 나머지를 구하는 문제

주요 Tip
1. 패턴을 보니 결국 피보나치 수열 하지만 이번엔 1,2,3,5,8 (2번째 1부터 시작)
2. memoization보다 빠른 것이 필요함.
3. bottom-up approach 가 더 빠를때가 있음. -> 둘다 알아야함.
"""

n = int(input()) 
cache = {}
def Fib(n):
    if n <= 2:
        return n
    if n in cache:
        return cache[n]
    else:
        value = Fib(n-1) + Fib(n-2)
        cache[n] = value
        return value
print(Fib(n))
    


