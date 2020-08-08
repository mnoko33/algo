import math

def solution(progresses, speeds):
    answer = []
    N = len(progresses)
    
    now_day = -1
    cnt = 1
    for i in range(N):
        progress = progresses[i]
        speed = speeds[i]
        DONE = 100
        remain = math.ceil((DONE - progress) / speed)

        if now_day == -1:
            now_day = remain
            continue
    
        if now_day >= remain:
            cnt += 1
        else:
            answer.append(cnt)
            now_day = remain
            cnt = 1
            
    return answer + [cnt]


print(solution([93, 99, 92, 93], [1, 1, 1, 1]))
    