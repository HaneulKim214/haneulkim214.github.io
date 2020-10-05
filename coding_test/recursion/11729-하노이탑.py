"""
주요 Tip
1.
"""

n = int(input())

tow1 = [n-i for i in range(n)]
tow2, tow3 = [0]*n, [0]*n
towers = [tow1, tow2, tow3]

# move 1 -> 3
# move 1 -> 2
# move 3 -> 2

f