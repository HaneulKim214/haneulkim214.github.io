"""
주요 Tip:
** sorted(key=) 엄청 강력하다. **

1. 문제들이 얼추 비슷비슷, 이번에도 먼저 정렬해야할것을 dictionary의 key로 만들고
key로 정렬, key가 같을경우 해당 key의 value 를 정렬해서 출력. 모든 (key, value[i])를 출력.
"""

n = int(input())

word_list = [input() for _ in range(n)]

d = {}
for word in word_list:
    word_length = len(word)
    if word_length in d:
        d[word_length].append(word)
    else:
        d[word_length] = [word]

sorted_by_word_length = sorted(d.items(), key=lambda x:x[0])

for tup in sorted_by_word_length:
    word_length = tup[0]
    words = tup[1]
    if len(words) == 1:
        print(words[0])
        continue
    else:
        for word in sorted(list(set(words))):
            print(word)