def solution(prices):
    answer = []
    N = len(prices)
    for i in range(N):
        price = prices[i]
        _answer = 0
        for j in range(i+1, N):
            _answer += 1
            if price > prices[j]:
                break
        answer.append(_answer)
    return answer