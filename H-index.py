def solution(citations):
    citations.sort()
    n = len(citations)
    h = n
    while True:
        for i in range(n):
            if citations[i] >= h and n - i >= h:
                return h
        h -= 1