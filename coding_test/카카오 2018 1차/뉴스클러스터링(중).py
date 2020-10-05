"""
주요 Tip
0. bool(re.match(pattern, string)) <-- 중요함!
     return True if match.
1. &(교집합), |(합집합), 등등 set() 데이터타입에 사용할수 있다.
2. {} != set()
"""


import re
from collections import Counter

def solution(str1, str2):
    A = []
    B = []
    
    for i in range(len(str1)):
        e1 = str1[i:i+2].lower()
        if bool(re.match("[a-z][a-z]", e1)):
            A.append(e1)
            
    for i in range(len(str2)):
        e2 = str2[i:i+2].lower()
        if bool(re.match("[a-z][a-z]", e2)):
            B.append(e2)
            
    A_set = set(A)
    B_set = set(B)
    # J(A,B) = len(A&B) / len(AUB)
    # When A,B = {} then J(A,B) = 1
    if len(A) == 0 and len(B) == 0:
        jacard_score = 1
    else:
        int_set = A_set & B_set
        union_set = A_set | B_set

        numerator = 0
        denominator = 0
        for int_value in int_set:
            numerator += min(A.count(int_value), B.count(int_value))

        for uni_value in union_set:
            denominator += max(A.count(uni_value), B.count(uni_value))

        jacard_score = numerator/denominator
    
    return int(jacard_score*65536)
