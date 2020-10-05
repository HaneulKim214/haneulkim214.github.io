"""
주요Tip:
1. sorted() 함수를 사용하여 먼저 X로 정렬후 Y로 정렬가능...
   ex: sorted(arr, key=lambda coord:(coord[0], coord[1]) )
2. print(*list) - print elements in list with single space
"""


# My solution
n = int(input())
arr = [[int(item) for item in input().split(" ")] for _ in range(n)]
d = {}
for a in arr:
    if a[0] in d:
        d[a[0]].append(a[1])
    else:
        d[a[0]] = [a[1]]
x_sorted_d = sorted(d.items(), key=lambda item:item[0])

for coord in x_sorted_d:
    X = coord[0]
    Y = coord[1]
    if len(Y) > 1:
        for y in Y.sort():
            print(X, y)
    else:
        print(X, Y[0])
        continue

# Others
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr = sorted(arr, key = lambda x : (x[0], x[1])  )

for coord in arr:
    print(*coord)