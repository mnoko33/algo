import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    heap = []
    stock -= 1
    for i in range(len(dates)):
        heapq.heappush(heap, -supplies[i])
        date = dates[i]
        if stock > date:
            continue
            
        while stock < date:
            answer += 1
            stock -= heapq.heappop(heap)

    while stock < k - 1:
        answer += 1
        stock -= heapq.heappop(heap)
        
    return answer