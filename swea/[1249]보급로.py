import sys
sys.stdin = open("1249.txt", "r")

# def DFS(S, G, cost):
#     global answer
#     for i in range(4):
#         nx = S[0] + dx[i]
#         ny = S[1] + dy[i]
#         if 0 <= nx < N and 0 <= ny < N:
#             if (nx, ny) == G:
#                 answer = min(answer, cost)
#                 continue
#             _cost = _map[nx][ny]

#             if cost + _cost >= answer:
#                 continue

#             if _visit[nx][ny] > cost + _cost:
#                 cost += _cost
#                 _visit[nx][ny] = cost
#                 DFS((nx, ny), G, cost)
#                 cost -= _cost
from collections import deque

for case in range(1, int(input()) + 1):
    N = int(input())
    _map = [list(map(int, input())) for _ in range(N)]
    _visit = [[0 for _ in range(N)] for _ in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    Q = deque()
    Q.append([0, 0])
    _visit[0][0] = 1
    while Q:
        [x, y] = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if _visit[nx][ny] == 0:
                    Q.append([nx, ny])
                    _visit[nx][ny] = _visit[x][y] + _map[nx][ny]
                    continue
                if _visit[nx][ny] > _visit[x][y] + _map[nx][ny]:
                    Q.append([nx, ny])
                    _visit[nx][ny] = _visit[x][y] + _map[nx][ny]

    print(f'#{case} {_visit[N-1][N-1] - 1}')