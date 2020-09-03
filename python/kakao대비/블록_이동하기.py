from collections import deque

def solution(board):
    N = len(board)
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    # 두번째 위치의 좌표, 방향, 시간
    Q = deque([[0, 1, 0, 0]])
    visited = [[[0,0] for _ in range(N)] for _ in range(N)]
    visited[0][1][0] = 1
    while Q:
        r, c, direction, cost = Q.popleft()
        print(r,c,direction,cost)
        if r == N-1 and c == N-1:
            return cost
        cost += 1
        # 그냥 이동
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            # 가로일 때 
            if direction == 0:
                # 경계 체크
                if nr < 0 or nc-1 < 0 or nr >= N or nc >= N:
                    continue
                # 벽 체크
                if board[nr][nc] == 1 or board[nr][nc-1] == 1:
                    continue

            # 세로일 때 
            if direction == 1:
                # 경계 체크
                if nr-1 < 0 or nc < 0 or nr >= N or nc >= N:
                    continue
                # 벽 체크
                if board[nr][nc] == 1 or board[nr-1][nc] == 1:
                    continue

            # 방문지 체크
            if visited[nr][nc][direction] == 1:
                continue

            visited[nr][nc][direction] = 1
            Q.append([nr, nc, direction, cost])

        # 대각선 회전
        if direction == 0:
            if r-1 >= 0 and c-1 >= 0 and board[r-1][c] == 0 and board[r-1][c-1] == 0:
                if visited[r][c][1] == 0:
                    visited[r][c][1] = 1
                    Q.append([r,c,1,cost])
                if visited[r][c-1][1] == 0:
                    visited[r][c-1][1] = 1
                    Q.append([r,c-1,1,cost])

            if r+1 < N and c-1 >= 0 and board[r+1][c] == 0 and board[r+1][c-1] == 0:
                if visited[r+1][c][1] == 0:
                    visited[r+1][c][1] = 1
                    Q.append([r+1,c,1,cost])
                if visited[r+1][c-1][1] == 0:
                    visited[r+1][c-1][1] = 1
                    Q.append([r+1,c-1,1,cost])

        if direction == 1:
            if r-1 >= 0 and c-1 >= 0 and board[r-1][c-1] == 0 and board[r][c-1] == 0:
                if visited[r][c][0] == 0:
                    visited[r][c][0] = 1
                    Q.append([r,c,0,cost])
                if visited[r-1][c][0] == 0:
                    visited[r-1][c][0] = 0
                    Q.append([r-1,c,0,cost])

            if r-1 >= 0 and c+1 < N and board[r][c+1] == 0 and board[r-1][c+1] == 0:
                if visited[r][c+1][0] == 0:
                    visited[r][c+1][0] = 1
                    Q.append([r,c+1,0,cost])
                if visited[r-1][c+1][0] == 0:
                    visited[r-1][c+1][0] = 1
                    Q.append([r-1,c+1,0,cost])

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [1, 1, 1, 1, 1, 1, 1, 0, 0], 
    [1, 1, 1, 1, 1, 1, 1, 1, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 1, 1, 1, 1, 1, 0, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1], 
    [0, 0, 1, 1, 1, 1, 1, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [1, 1, 1, 1, 1, 1, 1, 1, 0]
]
print(solution(board))