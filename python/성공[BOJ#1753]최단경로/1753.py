# 최단경로
import heapq
import sys
# input = sys.stdin.readline
sys.stdin = open('1753.txt', 'r')
INF = sys.maxsize

V,E = map(int, input().split(' '))
K = int(input())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int, input().split(' '))
    graph[u].append([w,v])

dist = [INF] * V
dist[K-1] = 0

def main():
    H = []
    heapq.heappush(H, (0, K))
    while H:
        # 가중치와 현재 노드
        W, now = heapq.heappop(H)

        # 현재 노드에서 갈 수 있는 노드 리스트
        # w: 가중치, v: 노드번호
        for (w,v) in graph[now]:
            if dist[now-1] + w < dist[v-1]:
                dist[v-1] = dist[now-1] + w
                heapq.heappush(H, (dist[v], v))

main()
for i in range(1, V+1):
    print("INF" if dist[i-1] == INF else dist[i-1])
