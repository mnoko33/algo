from collections import deque

def solution(numbers, target):
    N = len(numbers)
    Q = deque([[0, -1]])
    answer = 0
    while Q:
        acc, idx = Q.popleft()
        idx += 1
        if idx == N:
            if acc == target:
                answer += 1
            continue
        new_acc_1 = acc + numbers[idx]
        new_acc_2 = acc - numbers[idx]
        Q.append([new_acc_1, idx])
        Q.append([new_acc_2, idx])
    return answer