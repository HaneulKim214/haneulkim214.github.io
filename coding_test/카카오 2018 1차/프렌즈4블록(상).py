"""
주요 Tip

re.finditer(pattern, str) -> finds all positions where pattern is matched.

"""

def Pop(board, pop_dict):
    """remove according to pop_dict and return new_board with popped values represented as 0"""
    #{1:[(4,5)]} -> pop row=1col=4,5 and row=1col=4,5
    for row, col in pop_dict.items():
        for c in col: 
            board[row-1][c[0]-1] = 0 
            board[row-1][c[1]-1] = 0 

            board[row][c[0]-1] = 0
            board[row][c[1]-1] = 0
        
    return board


def solution(m, n, board):
    pop_dict = {}
    # 1. 2x2 들이 생기면 터진다. -> 2x2 를 알아차릴방법을 알아내자.
    board = [list(row) for row in board]

    for i in range(1, len(board)):
        row1 = board[i-1]
        row2 = board[i]
        for row_i in range(len(row1)-1):
            r1 = row1[row_i:row_i+2]
            r2 = row2[row_i:row_i+2]
            
            if r1 == r2:
                # popping --> row=i, column= row_1,row_2, row=i+1 column=row_1,row_2
                if i not in pop_dict:
                    pop_dict[i] = [(row_i+1, row_i+2)]
                else:
                    pop_dict[i].append((row_i+1, row_i+2)) 
    
    new_board = Pop(board, pop_dict)
    # 2. 빈자리를 채워준다 -> 위에서 떨어지는형식
    
    # 3. 1~2번 반복, 더이상 없다면 return "터져서 사라진 블록 수"  --> 재귀
    return new_board







# 재즐보프님 풀이
