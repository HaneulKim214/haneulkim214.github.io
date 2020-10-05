"""
주요 Tip
1. re.sub 사용법
   re.sub(pattern, replacestr_if_pattern_match, string)

2. eval() calculates mathematical operations that are written in string

"""


import re
d = {
    "S": '**1',
    "D": '**2',
    "T": '**3',
    "#":"*-1"
    }

def solution(dartResult):
    answer = ""
    # 아래 패턴이 (1st variable) 나온다면 뒤에 2nd variable
    # 처럼 스페이스 하나씩 넣어준다.
    for score in re.sub('([SDT][*#]?)', "\g<1> ", dartResult).split():
        if score[-1] == "*":
            if answer:
                answer = answer[:-1] + "*2+"
            score += "2"
        for key in d.keys():
            score = score.replace(key, d[key]) # key 가 score(string) 에 없다면 아예 안바뀜.
        answer += score + "+"
        
    return eval(answer[:-1])