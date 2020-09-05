from collections import deque

def solution(board):
    STRAIGHT = 100
    CORNER = 500
    N = len(board)
    DR = [0, 1, 0, -1]
    DC = [1, 0, -1, 0]
    visited = [[-1] * N for _ in range(N)]

    Q = deque([[0, 0, 0, 0], [0, 0, 0, 1]])
    visited[0][0] = 0
    while Q:
        r,c,cost,direction = Q.popleft()

        for d in range(4):
            nr = r + DR[d]
            nc = c + DC[d]
            # 경계체크
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue
            
            # 벽체크
            if board[nr][nc] == 1:
                continue

            # 후진은 제외
            if abs(direction - d) == 2:
                continue

            if direction == d:
                new_cost = cost + STRAIGHT
            else:
                new_cost = cost + STRAIGHT + CORNER
            
            if visited[nr][nc] == -1 or visited[nr][nc] >= new_cost:
                visited[nr][nc] = new_cost
                Q.append([nr, nc, new_cost, d])

    return visited[N-1][N-1]


board =	[[0, 0, 1], [0, 0, 0], [1, 1, 0]]
print(solution(board))