import math

def solution(progresses, speeds):
    def calculate_left_days(progresses):
        DONE = 100
        left_progresses = [DONE - progress for progress in progresses]
        return [math.ceil(left_progress / speed) for left_progress, speed in zip(left_progresses, speeds)]

    result = []
    day_dist = -1
    cnt = -1
    left_days = calculate_left_days(progresses)
    for left_day in left_days:
        if day_dist == -1:
            day_dist = left_day
            cnt = 1
            continue
        if day_dist >= left_day:
            cnt += 1
        else:
            result.append(cnt)
            day_dist = left_day
            cnt = 1
    result.append(cnt)
    return result


progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))