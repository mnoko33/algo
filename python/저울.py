# 과연 이게 greedy 문제인가...?

def solution(weights):
    weights.sort()
    answer = 1
    for weight in weights:
        if answer >= weight:
            answer += weight
    return answer