from collections import deque

def solution(n, vertex):
    G = [[] for _ in range(n+1)]
    for x,y in vertex:
        G[x].append(y)
        G[y].append(x)
    
    Q = deque([[1, 0]])

    visited = [0] * (n+1)
    visited[1] = 1

    cnt_v = 0
    max_dist = 0
    while Q:
        v, dist = Q.popleft()
        conn = [x for x in G[v] if not visited[x]]
        if not conn:
            if dist == max_dist:
                cnt_v += 1
            else:
                max_dist = dist
                cnt_v = 1
        else:
            for next_v in conn:
                if not visited[next_v]:
                    visited[next_v] = 1
                    Q.append([next_v, dist+1])
    return cnt_v