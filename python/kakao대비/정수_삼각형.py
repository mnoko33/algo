def solution(triangle):
    N = len(triangle)
    DP = [[-1] * N for _ in range(N)]
    DP[0][0] = triangle[0][0]
    for i in range(1, N): # 세로
        for j in range(i+1): # 가로
            if j == 0:
                before = [DP[i-1][0]]
            elif j == i:
                before = [DP[i-1][j-1]]
            else:
                before = [DP[i-1][j-1], DP[i-1][j]]
            DP[i][j] = triangle[i][j] + max(before)
    print(DP)
    return max(DP[N-1])

triangle = 	[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
solution(triangle)