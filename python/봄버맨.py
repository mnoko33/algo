from collections import deque

def main(R, C, N, MAP):
    def loop_MAP(callback_func):
        for r in range(R):
            for c in range(C):
                callback_func(r, c)

    def set_time(r, c):
        if MAP[r][c] >= 1:
            MAP[r][c] -= 1

    def set_bombs(r, c):
        if MAP[r][c] == 0:
            MAP[r][c] = 3
    
    def is_over_boundary(r, c):
        return r < 0 or c < 0 or r >= R or c >= C

    def explode_bombs(r, c):
        if MAP[r][c] != 1:
            return
        DR = [0, 1, 0, -1]
        DC = [1, 0, -1, 0]
        Q = deque([[r, c]])
        while Q:
            r, c = Q.popleft()
            if MAP[r][c] == 1:
                for d in range(4):
                    nr = r + DR[d]
                    nc = c + DC[d]
                    if is_over_boundary(nr, nc):
                        continue
                    if MAP[nr][nc] >= 1:
                        Q.append([nr, nc])
            MAP[r][c] = 0
                
    # 첫 1초는 아무것도 하지 않는다
    N -= 1
    loop_MAP(set_time)
    while N > 0:
        # 1초가 지난 후 폭탄 설치
        N -= 1
        loop_MAP(set_time)
        loop_MAP(set_bombs)
        # 시간이 다 지난 경우 종료
        if N == 0:
            break
        N -= 1
        loop_MAP(explode_bombs)
        loop_MAP(set_time)

    for row in MAP:
        print(''.join(['O' if x >= 1 else '.' for x in row]))


R, C, N = map(int, input().split())
MAP = []
for _ in range(R):
    MAP.append([0 if x == '.' else 3 for x in input()])
main(R, C, N, MAP)