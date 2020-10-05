"""
주요 Tip:
1. 또 비슷, 
   1.1 첫번째 조건으로 정렬
   1.2 첫번째조건 같은경우 2번째 조건으로 정렬.

같은 첫번째 조건을 가진 얘들을 배열에 넣어주고 dictionary 생성
{조건1:[v, v1, v2], 조건2:[v, v1, ..]}

1.1 조건으로 정렬.
1.2 조건에 있는 배열(2번째 조건)을 정렬하고 배열에 있는 아이템별로 첫번째조건이랑
붙여서 출력해준다.
"""


n = int(input())

lst = [(i, input().split(" ")) for i in range(n)]
sorted_lst = sorted(lst, key=lambda x:(int(x[1][0]), x[0]))
for tup in sorted_lst:
    print(tup[1][0], tup[1][1]) 