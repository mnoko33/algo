from collections import deque

def solution(board):
    N = len(board)
    STRAIGHT = 100
    CORNER = 500 + 100
    DR = [1, 0, -1, 0]
    DC = [0, 1, 0, -1]
    visited = [[-1] * N for _ in range(N)]
    # 출발지 초기화
    visited[0][0] = 0

    Q = deque([[0, 0, 0], [0, 0, 1]])

    while Q:
        r, c, direction = Q.popleft()
        now = visited[r][c]
        # i == new_direction
        for i in range(4):
            nr = r + DR[i]
            nc = c + DC[i]
            # 경계 체크
            if nr >= N or nc >= N or nr < 0 or nc < 0: 
                continue

            # 벽인 경우
            if board[nr][nc] == 1: 
                continue

            # 원래 온 곳으로 돌아오는 경우 제외
            if abs(direction - i) == 2: 
                continue 

            # 방문할 것인지 체크
            cost = STRAIGHT if direction == i else CORNER
            destination = visited[nr][nc]
            if destination == -1 or destination >= now + cost:
                visited[nr][nc] = now + cost
                Q.append([nr, nc, i])

    print(visited[N-1][N-1])
    return visited[N-1][N-1]

solution([[0,0,0],[0,0,0],[0,0,0]])
solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])
solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])
solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]])
