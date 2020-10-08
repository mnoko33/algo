from collections import deque

def main(R, C, K, _map):
    answer = 0
    DR = [0, 1, 0, -1]
    DC = [1, 0, -1, 0]

    def is_over_boundary(r, c):
        return r < 0 or c < 0 or r >= R or c >= C
    
    def is_visited(r, c):
        return _map[r][c] == 'v'

    def copy_map(_map):
        new_map = []
        for row in _map:
            new_map.append([x for x in row])
        return new_map

    START = [R-1, 0]
    END = [0, C-1]
    _map[START[0]][START[1]] = 'v'
    Q = deque([[_map, 0, START]])
    while Q:
        _map, cost, start = Q.popleft()
        if start == END and cost == K-1:
            answer += 1
            continue
        r, c = start
        for d in range(4):
            nr = r + DR[d]
            nc = c + DC[d]
            if is_over_boundary(nr, nc):
                continue
            if is_visited(nr, nc):
                continue
            if _map[nr][nc] == 'T':
                continue
            copied_map = copy_map(_map)
            copied_map[nr][nc] = 'v'
            Q.append([copied_map, cost + 1, [nr, nc]])

    return answer

R, C, K = map(int, input().split())
MAP = [[x for x in input()] for _ in range(R)]
print(main(R,C,K,MAP))