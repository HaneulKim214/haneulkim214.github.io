"""
주요 Tip:
1. Counter 의 most_common(n) 함수
2. round() 는 우리가 생각하는대로 작동하지 않음
   ex: round(1.5) = 2 , round(2.5) = 2
3. input() 대신 sys.stdin.readline() 사용 했더니 계속 실패하던게 됫다...ㅡㅡ;;
"""

from collections import Counter
import sys

def GetMode(lst):
    """More than one Mode -> return second smallest"""
    mc_lst = Counter(lst).most_common(2)
    if len(mc_lst) == 1:
        return mc_lst[0][0]
    if mc_lst[0][1] == mc_lst[1][1]:
        return mc_lst[1][0]
    else:
        return mc_lst[0][0]
        
n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(n)]
numbers.sort()
mean   = round(sum(numbers)/len(numbers))
median = numbers[len(numbers)//2]
mode   = GetMode(numbers)
rng  = max(numbers) - min(numbers)
print(mean)
print(median)
print(mode)
print(rng)