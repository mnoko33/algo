from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque()
    bridge_weight = deque()
    answer = 0
    while truck_weights:
        answer += 1
        for idx, truck_loc in enumerate(bridge):
            bridge[idx] = truck_loc - 1

        if bridge and bridge[0] == -1:
            bridge.popleft()
            bridge_weight.popleft()

        if sum(bridge_weight) + truck_weights[0] > weight:
            pulling = bridge[0]
            for idx, truck_loc in enumerate(bridge):
                bridge[idx] = truck_loc - pulling
            answer += pulling
        else:
            bridge.append(bridge_length-1)
            bridge_weight.append(truck_weights.pop(0))
        
        if len(truck_weights) == 0 and sum(bridge) > 0:
            answer += bridge.pop() + 1
    return answer