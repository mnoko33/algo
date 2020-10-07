from collections import deque

def main(N, M, graph_paper):
    DR = [0, 1, 0, -1]
    DC = [1, 0, -1, 0]
    
    def is_no_cheeze():
        for row in range(N):
            if sum(graph_paper[row]) > 0:
                return False
        return True
    
    def reset_air():
        for i in range(N):
            for j in range(M):
                if graph_paper[i][j] == 2:
                    graph_paper[i][j] = 0

    def set_external_air():
        Q = deque([[0, 0]])
        graph_paper[0][0] = 2
        while Q:
            r, c = Q.popleft()
            for d in range(4):
                nr = r + DR[d]
                nc = c + DC[d]
                if nr < 0 or nc < 0 or nr >= N or nc >= M:
                    continue
                if graph_paper[nr][nc] == 0:
                    graph_paper[nr][nc] = 2
                    Q.append([nr, nc])

    def is_contacted_cheeze(r, c):
        contacted_cnt = 0
        for d in range(4):
            nr = r + DR[d]
            nc = c + DC[d]
            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue
            if graph_paper[nr][nc] == 2:
                contacted_cnt += 1
        return contacted_cnt >= 2
    
    def find_contacted_cheeze():
        # cheeze_coords = []
        for i in range(N):
            for j in range(M):
                if graph_paper[i][j] == 1 and is_contacted_cheeze(i, j):
                    graph_paper[i][j] = 3
                    # cheeze_coords.append([i, j])
        # return cheeze_coords
    
    def remove_cheeze(cheeze_coords):
        for i in range(N):
            for j in range(M):
                if graph_paper[i][j] == 3:
                    graph_paper[i][j] = 0
        # for i, j in cheeze_coords:
        #     graph_paper[i][j] = 0
    
    cnt = 0
    while True:
        cnt += 1
        set_external_air()
        cheeze_coords = find_contacted_cheeze()
        remove_cheeze(cheeze_coords)
        reset_air()
        if is_no_cheeze():
            return cnt
    
N, M = map(int, input().split())
graph_paper = []
for _ in range(N):
    graph_paper.append(list(map(int, input().split())))
print(main(N, M, graph_paper))