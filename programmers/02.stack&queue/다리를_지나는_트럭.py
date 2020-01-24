def solution(bridge_length, weight, truck_weights):
    on_bridge = []
    answer = 1
    while truck_weights:

        truck = truck_weights[0]
        if len(on_bridge) == 0:
            answer += bridge_length
            on_bridge.append(truck_weights.pop(0))
        
        else:
            if sum(on_bridge) + truck >= weight:
                on_bridge.pop(0)
            else:
                answer += 1
                on_bridge.append(truck_weights.pop(0))
    
    return answer