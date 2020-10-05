"""
주요 Tip:
1. 시간을 다룰땐 가장 낮은단위로 변환후에 비교를 하고 그 후에 다시 시간(str) 으로 변환하기
2. 같은 시간이라도 우선순위를 매겨야 할경우 재귀를 사용하여 같은 숫자가 이미 있다면 +0.0001 를 더해줌으로서 우선순위를 미룬다. 
3. "%02d:%02d" % (hour, min) --> creating 0 left-padded integers.
"""

def TimeToMin(time):
    mins = int(time.split(":")[0])*60 + int(time.split(":")[1])
    return mins

def MinToTime(min):
    return "%02d:%02d" % (min//60, min%60)

def shuttleTime(n, t, start="09:00"):
    shuttles = [TimeToMin(start)]
    for n_i in range(n-1): #n-1 because we count first bus
        shuttles.append(shuttles[-1] + t)
    return shuttles

def DuplicateTime(time):
    if not time in integrate.keys():
        return time
    else:
        return DuplicateTime(time + 0.001)
    
def solution(n,t,m,timetable):
    global integrate
    crew = sorted([TimeToMin(t) for t in timetable])
    shuttles = shuttleTime(n,t)
    
    conTime = set(shuttles + crew)
    for c in set(crew):
        conTime.add(c-1)

    for con in sorted(list(conTime))[::-1]:
        
        print(sorted(list(conTime)))

        integrate=dict()
        for c in crew:
            integrate[DuplicateTime(c)] = 'crew'
        integrate[DuplicateTime(con)] = 'con'
        for sh in shuttles:
            integrate[DuplicateTime(sh)] = 'shuttle'

        print(integrate)

        waiting_line = []
        for time in sorted(integrate.keys()):
            if integrate[time] == 'crew':
                waiting_line.append('crew')
            elif 'shuttle' == integrate[time]:
                waiting_line = waiting_line[m:]
            elif 'con' == integrate[time]:
                waiting_line.append('con')
            print(waiting_line)
        if not 'con' in waiting_line:
            return MinToTime(con)