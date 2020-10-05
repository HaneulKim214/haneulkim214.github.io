"""
주요 Tip:
1. you always need a if statement to break recursion
2. line 10: n==0 을 추가해줘야 한다. Factorial(0) 이 들어올수도 있기에. 
"""

n = int(input())

def Factorial(n):
    if n == 1 or n==0:
        return 1
    return n*Factorial(n-1)
print(Factorial(n))