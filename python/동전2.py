def coin(k, coins):
    dp = [0] * (k+1)

    for coin in coins:
        if coin <= k:
            dp[coin] = 1

    for i in range(1, k+1):
        for coin in coins:
            if coin > i or dp[i - coin] == 0:
                continue
            if dp[i] == 0:
                dp[i] = dp[i - coin] + 1
            else:
                dp[i] = min(dp[i], dp[i-coin] + 1)

    return dp[-1] if dp[-1] > 0 else -1

n, k = map(int, input().split(' '))
coins = [int(input()) for _ in range(n)]
print(coin(k, list(set(coins))))