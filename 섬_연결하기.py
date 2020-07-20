def solution(n, costs):
    answer = 0
    visited = [costs[0][0]]
    while len(visited) < n:
        removed = []
        tmp_cost = 0xffff
        tmp_idx = -1
        tmp_num = -1
        for idx, cost in enumerate(costs):
            x, y, c = cost[0], cost[1], cost[2]
            if x in visited and y in visited:
                removed.append(idx)
                continue
            elif x not in visited and y not in visited:
                continue
            if tmp_cost > c:
                    tmp_cost = c
                    tmp_idx = idx   
                    if x in visited:
                        tmp_num = y
                    else:
                        tmp_num = x

        answer += tmp_cost
        removed.sort(reverse=True)
        for _removed in removed:
            costs.pop(_removed)
        
        visited.append(tmp_num)
        
    return answer


# 우선순위큐 사용
import heapq

def solution(n, costs):
    answer = 0
    visited = [0]
    costs = [[cost[2], cost[0], cost[1]] for cost in costs]
    heapq.heapify(costs)
    tmp = []
    while len(visited) < n:
        min_cost = heapq.heappop(costs)
        c, x, y = min_cost[0], min_cost[1], min_cost[2]
        if x in visited and y not in visited:
            visited.append(y)
            answer += c
            if tmp:
                for _tmp in tmp:
                    heapq.heappush(costs, _tmp)
                tmp = []
            
        elif x not in visited and y in visited:
            visited.append(x)
            answer += c
            if tmp:
                for _tmp in tmp:
                    heapq.heappush(costs, _tmp)
                tmp = []
            
        elif x not in visited and y not in visited:
            tmp.append(min_cost)
    return answer