import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('9376.txt', 'r')
from sys import stdin
input = stdin.readline
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def BFS():
    visited = [[-1] * w for _ in range(h)]
    while Q:
        x,y,cnt = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            if visited[nx][ny] >= 0:
                continue
            # 그냥 통로 or 죄수가 있는 공간
            if jail[nx][ny] == '.' or jail[nx][ny] == '$':
                visited[nx][ny] = cnt
                Q.appendleft((nx, ny, cnt))
                continue
            # 문
            if jail[nx][ny] == '#':
                visited[nx][ny] = cnt+1
                Q.append((nx, ny, cnt+1))
                continue
    return visited

for _ in range(int(input())):
    h,w = map(int, input().split(' '))
    # 맵 확장하기
    jail = []
    jail.append(list('.' * (w + 2)))
    for _ in range(h):
        jail.append(list('.'+input().strip()+'.'))
    jail.append(list('.' * (w + 2)))
    h += 2
    w += 2
    # 죄수 위치
    prisoner = []
    for i in range(h):
        for j in range(w):
            if jail[i][j] == '$':
                prisoner.append((i, j, 0))
    # 상근, 죄수1, 죄수2
    p0 = (0, 0, 0)
    p1 = prisoner[0]
    p2 = prisoner[1]

    Q = deque()
    
    Q.append(p0)
    visited_0 = BFS()

    Q.append(p1)
    visited_1 = BFS()
    
    Q.append(p2)
    visited_2 = BFS()
    
    cnt = 0xffff
    for i in range(h):
        for j in range(w):
            if jail[i][j] == '*':
                continue

            temp = visited_0[i][j] + visited_1[i][j] + visited_2[i][j]
            if jail[i][j] == "#":
                temp -= 2
            cnt = min(temp, cnt)
    print(cnt)