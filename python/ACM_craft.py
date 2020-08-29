from collections import deque

for _ in range(int(input())):
    N, K = list(map(int, input().split(' ')))
    D = [0] + list(map(int, input().split(' ')))
    G = [[] for _ in range(N + 1)]
    in_degree = [0 for _ in range(N + 1)]
    for _ in range(K):
        prev, to = list(map(int, input().split(' ')))
        G[prev].append(to)
        in_degree[to] += 1

    W = int(input())
    Q = deque()
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            Q.append(i)

    DP = [x for x in D]
    while Q:
        x = Q.popleft()
        y_list = G[x]

        for y in y_list:
            in_degree[y] -= 1
            DP[y] = max(DP[y], DP[x] + D[y])
            if in_degree[y] == 0:
                Q.append(y)
                
    print(DP[W])
