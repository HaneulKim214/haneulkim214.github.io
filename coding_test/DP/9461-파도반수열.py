# 점화식을 찾는게 가장 우선이다.
# starting from n=5 
cache = {}
cache[0] = 1
cache[1] = 1
cache[2] = 1
cache[3] = 2
cache[4] = 2

def GetTriLength(n):
    
    if n in cache:
        return cache[n]
    else:
        value = GetTriLength(n-1) + GetTriLength(n-5)
        cache[n] = value
        return value


for i in range(int(input())):
    n = input()
    print(GetTriLength(n))