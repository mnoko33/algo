from collections import deque

def solution(n, weak, dist):
    D = len(dist)
    d = D-1
    Q = deque([[weak,d]])
    while Q:
        weak, d = Q.popleft()
        max_l = 1000000
        # idx of weak
        weak_list = []
        for i in range(len(weak)):
            start = weak[i]
            coverage = start + dist[d]
            new_weak = []
            for j in range(len(weak)):
                target = weak[j] if weak[j] >= start else n + weak[j]
                if target > coverage:
                    new_weak.append(weak[j])
            
            if new_weak == []:
                return D-d

            if d == 0:
                break
            new_weak.sort()
            if new_weak not in weak_list:
                max_l = min(len(new_weak), max_l)
                if len(new_weak) == max_l:
                    weak_list.append(new_weak)

        for _weak in weak_list:   
            Q.append([_weak, d-1])
    return -1