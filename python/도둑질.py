def solution(money):
    N = len(money)
    dp = []
    for i in range(N):
        if i == 0:
            including_first = money[i]
            excluding_first = 0
        elif i == 1:
            including_first = 0
            excluding_first = money[i]
        elif i == 2:
            including_first = dp[0][0] + money[i]
            excluding_first = money[i]
        else:
            including_first = max(dp[i-2][0], dp[i-3][0]) + money[i]
            excluding_first = max(dp[i-2][1], dp[i-3][1]) + money[i]

        dp.append([including_first, excluding_first])

    dp[-1][0] = 0
    return max([max(x, y) for x,y in dp])