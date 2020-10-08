def solution(N):
    if N == 1:
        return 1
    if N == 2:
        return 2
    table_dp = [0] * (N+1)
    table_dp[1] = 1
    table_dp[2] = 2
    for i in range(3, N+1):
        table_dp[i] = table_dp[i-1] + table_dp[i-2]
    return table_dp[N]

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))