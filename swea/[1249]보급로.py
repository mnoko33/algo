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

# from collections import deque

# for case in range(1, int(input()) + 1):
#     N = int(input())
#     _map = [list(map(int, input())) for _ in range(N)]
#     _visit = [[0 for _ in range(N)] for _ in range(N)]
#     dx = [-1, 0, 1, 0]
#     dy = [0, 1, 0, -1]
    
#     Q = deque()
#     Q.append([0, 0])
#     _visit[0][0] = 1
#     while Q:
#         [x, y] = Q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < N and 0 <= ny < N:
#                 if _visit[nx][ny] == 0:
#                     Q.append([nx, ny])
#                     _visit[nx][ny] = _visit[x][y] + _map[nx][ny]
#                     continue
#                 if _visit[nx][ny] > _visit[x][y] + _map[nx][ny]:
#                     Q.append([nx, ny])
#                     _visit[nx][ny] = _visit[x][y] + _map[nx][ny]

#     print(f'#{case} {_visit[N-1][N-1] - 1}')


# 우선순위큐 사용해보기 (최적화x)
import heapq

for case in range(1, int(input()) + 1):
    N = int(input())
    _map = [list(map(int, input())) for _ in range(N)]
    _visit = [[0 for _ in range(N)] for _ in range(N)]
    _map[0][0] = 0xffff
    _visit[0][0] = 1
    start = [0, 0, 0] # cost, x, y
    end = [N-1, N-1]
    Q = [start]
    answer = 0
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]
    while Q:
        v = heapq.heappop(Q)
        for i in range(4):
            nx = v[1] + dx[i]
            ny = v[2] + dy[i]
            if nx == N-1 and ny == N-1:
                answer = v[0]
                Q = []
                break
            if 0 <= nx < N and 0 <= ny < N and _visit[nx][ny] == 0:
                _visit[nx][ny] = 1
                heapq.heappush(Q, [v[0] + _map[nx][ny], nx, ny])
    print(f'#{case} {answer}')