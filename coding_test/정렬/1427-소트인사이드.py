"""
주요 Tip:
1. 입력이 "12345" 이런식으로 주어지는지 모름... 문제를 제대로 읽자.
"""

lst = []
for l in input():
    lst.append(int(l))
sorted_lst = sorted(lst, reverse=True)
print("".join([str(item) for item in sorted_lst]))