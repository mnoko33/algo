import sys
sys.stdin = open('1486.txt', 'r')

INF = 0xffff
from collections import deque

def char2Int(x):
    if x.isupper():
        return ord(x) - 65
    else:
        return ord(x) - 71

N,M,T,D = map(int, input().split(' '))
Map = [[char2Int(x) for x in input()] for _ in range(N)]
GO = [[INF] * M for _ in range(N)]
COME = [[INF] * M for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 가는 최소값
goQ = deque()
GO[0][0] = 0
goQ.append((0,0))
while goQ:
    x,y = goQ.popleft()
    now = Map[x][y]
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        target = Map[nx][ny]
        if abs(target - now) > T:
            continue
        cost = 1 if now >= target else (now - target) ** 2
        if cost > D:
            continue
        if GO[x][y] + cost < GO[nx][ny]:
            GO[nx][ny] = GO[x][y] + cost
            goQ.append((nx, ny))

# 오는 최소값
comeQ = deque()
COME[0][0] = 0
comeQ.append((0,0))
while comeQ:
    x,y = comeQ.popleft()
    now = Map[x][y]
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        target = Map[nx][ny]
        if abs(target - now) > T:
            continue
        cost = 1 if now <= target else (now - target) ** 2
        if cost + GO[nx][ny] > D:
            continue
        if COME[x][y] + cost < COME[nx][ny]:
            COME[nx][ny] = COME[x][y] + cost
            comeQ.append((nx, ny)) 

h = 0
for i in range(N):
    for j in range(M):
        temp = GO[i][j] + COME[i][j]
        if temp > D:
            continue
        h = max(h, Map[i][j])
print(h)