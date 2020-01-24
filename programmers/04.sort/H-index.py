def solution(citations):
    answer = 0
    citations.sort()
    N = len(citations)
    for i in range(N):
        h = citations[i]
        if N - i >= h and i < h:
            answer = max(h, answer)
    
    return answer