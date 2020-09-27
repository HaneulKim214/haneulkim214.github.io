"""
주요 Tip:
없음... Tooo Easy peasy lemon squezy   
"""

n = input()
for i in range(int(n)):
    R, S = input().split(" ")
    new_S = ""
    for letter in S:
        new_S += letter*int(R)
    print(new_S)
        
