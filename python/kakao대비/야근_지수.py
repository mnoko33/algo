import heapq

def solution(n, works):
    works = [-work for work in works]
    heapq.heapify(works)
    for i in range(n):
        if not works:
            return 0
        work = heapq.heappop(works)
        if work < -1:
            heapq.heappush(works, work+1)
    return sum([work ** 2 for work in works])