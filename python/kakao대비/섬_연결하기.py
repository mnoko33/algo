import heapq

def solution(n, costs):
    visited = [0] * (n)
    hq = [[0,0]]
    G = [[] for _ in range(n)]
    for x,y,cost in costs:
        G[x].append([cost,y])
        G[y].append([cost,x])

    answer = 0
    while hq:
        cost, v = heapq.heappop(hq)
        if visited[v]:
            continue

        visited[v] = 1
        answer += cost
        if sum(visited) == n:
            return answer
        for cost, conn_v in G[v]:
            if not visited[conn_v]:
                heapq.heappush(hq, [cost, conn_v])

n = 4
costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
print(solution(n, costs))