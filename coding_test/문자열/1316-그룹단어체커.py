import re

"""
문자열 문제에는 re 라이버리가 엄청 유용하게 쓰일듯. --> look into it.
"""
n = input()
def IsGroupWord(word):
    """Checks whether inputted string is a group word"""
    for letter in set(word):
        letter_indexes = [m.start() for m in re.finditer(letter, word)]

        for i,j in zip(letter_indexes[:-1], letter_indexes[1:]):
            if j-i != 1:
                return False
    return True

group_word_cnt = 0

for line in range(int(n)):
    word = input()
    if IsGroupWord(word):
        group_word_cnt += 1
print(group_word_cnt)
    