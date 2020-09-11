ef solution(n):
    answer = [[0] * n for _ in range(n)]
    DR = [1, 0, -1]
    DC = [0, 1, -1]
    x = 1
    d = 0
    r = -1
    c = 0
    N = n
    while N > 0:
        cnt_n = N
        while cnt_n > 0:
            r += DR[d]
            c += DC[d]
            answer[r][c] = x
            cnt_n -= 1
            x += 1
            if cnt_n <= 0:
                break
        N -= 1
        d = (d+1) % 3

    result = []
    for i in range(n):
        result += answer[i][:i+1]
    return result