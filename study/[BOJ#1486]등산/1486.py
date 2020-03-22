import sys
sys.stdin = open('1486.txt', 'r')

INF = sys.maxsize
from collections import deque
import heapq

N,M,T,D = map(int, input().split(' '))
Map = [[ord(x)-65 for x in input()] for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
G = [[[[INF] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
# init
for x in range(N):
    for y in range(M):
        now = Map[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            target = Map[nx][ny]
            # 갈 수 없는 곳
            if abs(target - now) > T:
                continue
            cost = 1 if now >= target else (now - target) ** 2
            # 가기 전에 어두워지는 상황
            if cost > D:
                continue
            G[x][y][nx][ny] = cost

# 중간지점
for dx in range(N):
    for dy in range(M):
        # 출발지점
        for nx in range(N):
            for ny in range(M):
                # 도착지점
                for tx in range(N):
                    for ty in range(M):
                        middle = G[nx][ny][dx][dy] + G[dx][dy][tx][ty]
                        if middle > D:
                            continue
                        G[nx][ny][tx][ty] = min(G[nx][ny][tx][ty], middle)
print(G[0][0][0][0])