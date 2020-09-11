def solution(m, n, puddles):
    _map = [[0] * m for _ in range(n)]
    _map[0][0] = 1
    for i in range(n):
        for j in range(m):
            if [i, j] == [0, 0] or [j+1, i+1] in puddles:
                continue
            if i == 0:
                _map[i][j] = _map[i][j-1]
            elif j == 0:
                _map[i][j] = _map[i-1][j]
            else:
                _map[i][j] = (_map[i-1][j] + _map[i][j-1]) % 1000000007

    return _map[n-1][m-1] % 1000000007

m = 4
n = 3
puddles = [[2, 2]]
print(solution(m, n, puddles))