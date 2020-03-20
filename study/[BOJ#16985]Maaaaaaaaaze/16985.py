import sys
sys.stdin = open('16985.txt', 'r')
from collections import deque

maze = [[list(map(int, input().split(' '))) for _ in range(5)] for _ in range(5)]
# 입구 [0][0][0]
# 출구 [5][5][5]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, 0, -1, 0]
dz = [0, 0, 0, 1, 0, -1]

def search(target):
    global answer
    # 입구 혹은 출구가 막혀 있는 경우
    if target[0][0][0] == 0 or target[4][4][4] == 0:
        return -1
    INF = 0xffff
    visited = [[[INF] * 5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = 0 
    Q = deque()
    Q.append((0, 0, 0))
    while Q:
        i, j, k = Q.popleft()
        # 더 이상 볼 필요가 없는 문제
        if visited[i][j][j] > answer:
            return -1
        for idx in range(6):
            ni = i + dx[idx]
            nj = j + dy[idx]
            nk = k + dz[idx]
            # 경계체크
            if ni < 0 or nj < 0 or nk < 0 or ni >= 5 or nj >= 5 or nk >= 5:
                continue
            if target[ni][nj][nk] == 1 and visited[i][j][k] + 1 < visited[ni][nj][nk]:
                visited[ni][nj][nk] = visited[i][j][k] + 1
                Q.append((ni, nj, nk))

    if visited[4][4][4] == INF:
        return -1
    else:
        return visited[4][4][4]

# arr를 넣으면 arr를 포함한 4개의 회전 결과 값을 리턴
def rotate(arr):
    result = []
    result.append(arr)
    vacant = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    # 총 세번 회전해야함
    for _ in range(3):
        vacant = [[[0] * 5 for _ in range(5)] for _ in range(5)]
        for i in range(5):
            for j in range(5):
                
                vacant[j][4-i] = result[-1][i][j]
        result.append(vacant)
    
    return result

def perm(arr, idx):
    global answer

    if idx == 4:
        temp = search(arr)
        if temp >= 0:
            answer = min(temp, answer)
        return

    for i in range(idx, 5):
        arr[idx], arr[i] = arr[i], arr[idx]
        perm(arr, idx + 1)
        arr[idx], arr[i] = arr[i], arr[idx]

global answer
answer = 0xffff
# 1층
maze_1 = rotate(maze[0])
# 2층
maze_2 = rotate(maze[1])
# 3층
maze_3 = rotate(maze[2])
# 4층
maze_4 = rotate(maze[3])
# 5층
maze_5 = rotate(maze[4])

for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                for e in range(4):
                    perm([maze_1[a], maze_2[b], maze_3[c], maze_4[d], maze_5[e]], 0)

if answer == 0xffff:
    print(-1)
else:
    print(answer)
