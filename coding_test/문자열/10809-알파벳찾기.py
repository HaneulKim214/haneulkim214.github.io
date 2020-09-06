"""
주요 Tip:
1. ord(), chr()
2. modular arithmetic.
3. find() 함수. --> return index of first occurence of substr if
   found else return -1
   ex: "abbbc".find("b") = 1 since index=1 is 
        first occurence of "b"
"""

word = input()
alphabet_list = ["-1"]*26
for letter in word:
    alphabet_list[ord(letter) % 97] =  str(word.find(letter))

print(" ".join(alphabet_list))
