def solution(n):
    result = [0, 1, 2]
    for i in range(3, n+1):
        result.append((result[i-1] + result[i-2]) % 1000000007)
    return result[n] % 1000000007