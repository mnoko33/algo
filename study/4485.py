import sys
sys.stdin = open('4485.txt', 'r')

from collections import deque
INF = 0xffff
problem = 1
while True:
    N = int(input())
    if N == 0:
        break
    cage = []
    visited = [[INF] * N for _ in range(N)]
    for _ in range(N):
        cage.append(list(map(int, input().split(' '))))
    Q = deque()
    Q.append((0, 0))
    visited[0][0] = cage[0][0]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while Q:
        x, y = Q.popleft()
        cost = visited[x][y]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if visited[nx][ny] == INF or cost + cage[nx][ny] < visited[nx][ny]:
                visited[nx][ny] = cost + cage[nx][ny]
                Q.append((nx, ny))
    print('Problem {}: {}'.format(problem, visited[N-1][N-1]))
    problem += 1