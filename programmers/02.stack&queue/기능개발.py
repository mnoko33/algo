def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 1
        progress = progresses.pop(0)
        speed = speeds.pop(0)
        
        if (100-progress) % speed:
            day = (100-progress) // speed + 1
        else:
            day = (100-progress) // speed
            
        for idx, val in enumerate(progresses):
            progresses[idx] = val + speeds[idx] * day
        
        if progresses == []:
            answer.append(cnt)
            break
        else:
            while progresses:
                if progresses[0] >= 100:
                    progresses.pop(0)
                    speeds.pop(0)
                    cnt += 1
                else:
                    break
        answer.append(cnt)
    return answer

progresses = [93,30,55]
speeds = [1,30,5]
print(solution(progresses, speeds))