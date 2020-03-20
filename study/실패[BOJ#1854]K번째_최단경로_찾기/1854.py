import heapq
import sys
sys.stdin = open('1854.txt', 'r')


n, m, k = map(int, input().split(' '))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split(' '))
    graph[a].append([b,c])

dist_list = [[] for _ in range(n+1)]
h = [] # heap
start = 1
for target, cost in graph[start]:
    heapq.heappush(dist_list[target], cost)
    heapq.heappush(h, [cost, target])

while h:
    now_cost, now = heapq.heappop(h)
    for target, cost in graph[now]:
        if len(dist_list[target]) == k:
            continue
        heapq.heappush(dist_list[target], (now_cost + cost))
        heapq.heappush(h, [(now_cost + cost), target])

for i in range(1, n+1):
    if len(dist_list[i]) == 0:
        print(-1)
    else:
        print(dist_list[i][k-1])
