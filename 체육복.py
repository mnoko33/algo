def solution(n, lost, reserve):
    students = [1] * n
    for lost_idx in lost:
        students[lost_idx-1] -= 1
    for reserve_idx in reserve:
        students[reserve_idx-1] += 1
    for idx, cnt in enumerate(students):
        if cnt == 1 or cnt == 0:
            continue
        if idx == 0:
            if students[idx+1] == 0:
                students[idx] -= 1
                students[idx+1] += 1
        elif idx == n-1:
            if students[idx-1] == 0:
                students[idx] -= 1
                students[idx-1] += 1
        else:
            if students[idx-1] == 0:
                students[idx] -= 1
                students[idx-1] += 1
                continue
            if students[idx+1] == 0:
                students[idx] -= 1
                students[idx+1] += 1
    answer = 0
    for student in students:
        if student >= 1:
            answer += 1
    return answer