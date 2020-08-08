from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    Q = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    now_weight = 0
    while Q:
        answer += 1
        now_weight -= Q.popleft()
        if truck_weights:
            if now_weight + truck_weights[0] <= weight:
                new_weight = truck_weights.popleft()
                now_weight += new_weight
                Q.append(new_weight)
            else:
                Q.append(0)

    return answer



print(solution(2, 10, [7, 4, 5, 6]))