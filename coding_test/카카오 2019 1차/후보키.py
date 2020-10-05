import itertools
import pandas as pd

def solution(relation):
    df = pd.DataFrame(relation)
    len_df = len(df)
    columns = df.columns.tolist()
    
    unique_candidates = []
    for col in columns:
        if len(df.groupby([col]).count()) == len_df:
            unique_candidates.append(col)
            
    columns = list(set(columns) - set(unique_candidates))

    del_columns = []
    for i in range(2, len(relation[0]) + 1 ):
        if len(columns) < i:
            break
        i_combinations = list(itertools.combinations(columns, i))

        for cols in i_combinations:
            if len(df.groupby(list(cols))) == len_df:
                del_columns.extend(list(cols))
                unique_candidates.append(cols)
        columns = list(set(columns) - set(del_columns))
    return len(unique_candidates)



orders_dict = reduce(lambda l,r: l+r, [Counter(list(ord)) for ord in orders])

over2_orders_dict = {}
for menu, cnt in orders_dict.items():
    if cnt >=2:
        over2_orders_dict[menu] = cnt
print(over2_orders_dict)

course_menu = list(over2_orders_dict.keys())
print(course_menu)

# all_possible_comb = list(itertools.combinations(course_menu ))



def CheckMatch(ind_info_list, ind_q_list):
    for i,q in zip(ind_info_list, ind_q_list):
        if q == "-":
            continue
        if i != q:
            return False
    return True



def solution(info, query):
    answer = []
    
    for q in query:
        ind_q_list = [item for item in q.split(" ") if item != "and"]
        ind_q_list[-1] = int(ind_q_list[-1])
        cnt = 0
        for i in info:
            ind_info_list = i.split(" ")
            ind_info_list[-1] = int(ind_info_list[-1])
            
            if ind_info_list[-1] >= ind_q_list[-1]:
                if CheckMatch(ind_info_list[:-1], ind_q_list[:-1]):
                    cnt +=1
                
        answer.append(cnt)
            
    return answer