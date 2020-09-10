from collections import deque

def solution(n, computers):
    G = [[] for _ in range(n)]
    visited = [0] * n
    for i, computer in enumerate(computers):
        for j in range(n):
            if computers[i][j] == 1:
                G[i].append(j)
    cnt = 0
    for i in range(n):
        if visited[i]:
            continue
        cnt += 1
        visited[i] = 1
        Q = deque([i])
        while Q:
            v = Q.popleft()
            edges = G[v]
            for edge in edges:
                if visited[edge]:
                    continue
                visited[edge] = 1
                Q.append(edge)
    return cnt

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))