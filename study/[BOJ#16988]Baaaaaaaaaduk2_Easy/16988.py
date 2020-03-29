import sys
sys.stdin = open('16988.txt', 'r')
from collections import deque

global N
global M
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 몇점을 얻는지 체크하는 함수
def check():
    temp_answer = 0
    global N
    global M
    Q = deque()
    # 바둑판 == temp_board
    for i in range(N):
        for j in range(M):
            # 검은 돌일 때 탐색 시작
            if temp_board[i][j] == 2:
                temp = [(i,j)]
                Q.append((i,j))
                while Q:
                    x,y = Q.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 < nx or 0 < ny or nx >= N or ny >= M:
                            continue
                        # 만약 빈칸이 있을 경우 탐색 취소
                        if temp_board[nx][ny] == 0:
                            Q = deque()
                            temp = []
                            break
                        if temp_board[nx][ny] == 2:
                            if (nx, ny) in temp:
                                continue
                            else:
                                Q.append((nx,ny))
                                temp.append((nx,ny))
                # 죽일 게 있다면
                if len(temp) > 0:
                    temp_answer += len(temp)
                    # 죽인걸로 처리
                    for x,y in temp:
                        temp_board[x][y] = 9
                temp = []
    print('>>>', temp_answer)
    return temp_answer

possible = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            possible.append((i,j))

answer = 0
for i in range(len(possible)):
    for j in range(len(possible)):
        if i < j:
            # temp_board 초기화
            temp_board = [[0] * M for _ in range(N)]
            for temp_i in range(N):
                for temp_j in range(M):
                    temp_board[temp_i][temp_j] = board[temp_i][temp_j]
            # 선택한 두 돌
            x1, y1 = possible[i]
            x2, y2 = possible[j]
            # 돌 두기
            temp_board[x1][y1] = 1
            temp_board[x2][y2] = 1
            # 체크
            print(x1, x2, y1, y2)
            if x1 == 0 and y1 == 3 and x2 == 2 and y2 == 0:
                print('=====================')
            answer = max(answer, check())
print(answer)