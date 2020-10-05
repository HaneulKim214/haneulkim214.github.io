cache = {}

def Fib(n):
    if n in cache: # use memo if stored.
        return cache[n]
    if n <= 2:
        return 1
    else:
        value = Fib(n-1) + Fib(n-2)
        cache[n] = value #memo then return value
        return value