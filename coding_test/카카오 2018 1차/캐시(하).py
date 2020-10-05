"""
주요 Tip
1. 이번문제는 문제자체를 이해하는게 가장 힘들었음. -> 문제를 잘 읽고 제대로 이해하자.
2.막혔을땐 손으로 풀어보면 가장 도움이 되는듯.
"""


# 1차 풀이

# 왜이렇게 쉽나 했더니...

# cache = [A,B,C] 가 존재하고 다음 도시가 A 라면 순서가 바뀌어야함 --> [B,C,A]
# 이 로직을 else statement 에 추가해준다.
def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    for city in cities:
        city = city.lower()
        if city not in cache:
            answer += 5
        else:
            answer += 1
        cache.append(city)
        if len(cache) > cacheSize:
            cache.pop(0)
    return answer


# 2차 풀이
# 45번 라인의 continue 없이하다 한참 고민했는데 만약 [A,B,C]가 있고 A 가 들어온다면 [B,C,A]로 바뀌고
# 다음라인 46에서 다시 넣어줄필요가 없음.
def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    for city in cities:
        
        city = city.lower()
        if city not in cache:
            answer += 5
        else:
            answer += 1
            cache.remove(city)
            cache.append(city)
            continue
        cache.append(city)
        if len(cache) > cacheSize:
            cache.pop(0)
            
    return answer

