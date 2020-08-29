from collections import deque

def main(N, K):
    if N == K:
        return 0

    visited = [False for _ in range(100001)]
    MIN_POS = 0
    MAX_POS = 100000

    def is_visited(pos):
        return visited[pos]
    
    Q = deque([[N, 0]])
    while Q:
        pos, time = Q.popleft()
        new_pos_list = [pos - 1, pos + 1, pos * 2]
        new_time = time + 1
        for new_pos in new_pos_list:
            if new_pos == K:
                return new_time
            if new_pos > MIN_POS and new_pos <= MAX_POS and is_visited(new_pos) == False:
                Q.append([new_pos, new_time])
                visited[new_pos] = True

N, K = list(map(int, input().split(' ')))
print(main(N, K))
