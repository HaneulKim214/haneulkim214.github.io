# Check if it can be divisible by 5,3,2

def GetDivisibleList(n):
    lst = []
    if n % 5 == 0:
        lst.append(5)
    elif n % 3 == 0:
        lst.append(3)
    elif n % 2 == 0:
        lst.append(2)
    return lst

n = 26
divisible_lst = GetDivisibleList(n)
if len(divisible_lst) == 0:
    n -= 1
    
else:
    n = n // max(divisible_lst)