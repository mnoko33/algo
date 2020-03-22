import sys
sys.stdin = open('5719.txt', 'r')
INF = sys.maxsize
import heapq
from collections import deque

while True:
    N,M = map(int, input().split(' '))
    # 테스트 케이스 종료 조건
    if N == 0 and M == 0:
        break
    # S: 출발
    # D: 도착
    global S
    global D
    S,D = map(int, input().split(' '))
    G = [[] for _ in range(N)]
    visited = [[] for _ in range(N)]
    for _ in range(M):
        u,v,p = map(int, input().split(' '))
        G[u].append((p, v))

    dist = [INF] * N
    dist[S] = 0
    PQ = []
    heapq.heappush(PQ, (0, S))
    while PQ:
        now_p, now_v = heapq.heappop(PQ)
        for p, v in G[now_v]:
            if p + now_p == dist[v]:
                visited[v].append(now_v)
                dist[v] = p + now_p
                heapq.heappush(PQ, (p + now_p, v))
                
            if p + now_p < dist[v]:
                visited[v] = [now_v]
                dist[v] = p + now_p
                heapq.heappush(PQ, (p + now_p, v))

    Q = deque()
    Q.append(D)
    while Q:
        v = Q.popleft()
        for x in visited[v]:
            g = G[x]
            l = len(G[x])
            Q.append(x)
            for i in range(l):
                if g[i][1] == v:  
                    G[x].pop(i)
                    break

    dist = [INF] * N
    dist[S] = 0
    PQ = []
    heapq.heappush(PQ, (0, S))
    while PQ:
        now_p, now_v = heapq.heappop(PQ)
        for p, v in G[now_v]:
            if p + now_p <= dist[v]:
                dist[v] = p + now_p
                heapq.heappush(PQ, (p + now_p, v))

    print(-1 if dist[D] == INF else dist[D])