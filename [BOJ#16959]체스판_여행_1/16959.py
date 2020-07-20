import sys
sys.stdin = open('16959.txt', 'r')
from collections import deque
from heapq import heappop, heappush 

# 8
knightX = [-2, -2, -1, -1, 1, 1, 2, 2]
knightY = [1, -1, 2, -2, 2, -2, 1, -1]
# 4
bishopX = [1, 1, -1, -1] 
bishopY = [1, -1, 1, -1]
# 4
rookX = [0, 1, 0, -1]
rookY = [1, 0, -1, 0]

def move(s, e): # 시작점과 도착점
    global N
    Q = deque()
    H = []
    global N
    sx = s[0]
    sy = s[1]
    ex = e[0]
    ey = e[1]
    Q.append((0, sx, sy))
    while Q:
        cost, x,y = Q.popleft()
        # 나이트 이동
        # 비숍 이동
        # 룩 이동
global N
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
route = [[[0,0,0] for _ in range(N)] for _ in range(N)] # 나이트, 비숍, 룩 순

