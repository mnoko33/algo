import sys
sys.stdin = open('1854.txt', 'r')

import heapq
n, m, k = map(int, input().split(' '))
graph = [[] for _ in range(n)]
for _ in range(m):
    a,b,c = map(int, input().split(' '))
    graph[a-1].append([b-1,c])

dist_list = [[] for _ in range(n)]
h = [] # heap
heapq.heappush(dist_list[0], 0)
heapq.heappush(h, [0, 0])

while h:
    now_cost, now = heapq.heappop(h)
    for target, cost in graph[now]:
        # 이미 거리 k개가 등록됐을 때
        if len(dist_list[target]) < k:
            heapq.heappush(dist_list[target], -1 * (now_cost + cost))
            heapq.heappush(h, [(now_cost + cost), target])
        elif len(dist_list[target]) >= k and -1 * dist_list[target][0] > now_cost + cost:
            heapq.heappop(dist_list[target])
            heapq.heappush(dist_list[target], -1 * (now_cost + cost))
            heapq.heappush(h, [(now_cost + cost), target])
        else:
            continue

for dist in dist_list:
    if len(dist) == k:
        print(-dist[0])
    else:
        print(-1)
