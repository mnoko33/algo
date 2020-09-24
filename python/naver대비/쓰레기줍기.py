def solution(N, M, map):
    for i in range(N):
        for j in range(M):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                map[i][j] += map[i][j-1]
            elif j == 0:
                map[i][j] += map[i-1][j]
            else:
                map[i][j] += max(map[i][j-1], map[i-1][j])

    return map[N-1][M-1]