import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    h=[]
    for idx, date in enumerate(dates):
        heapq.heappush(h, -supplies[idx])
        if idx == len(dates) - 1:
            while stock < k:
                answer += 1
                stock -= heapq.heappop(h)
        else:
            if stock < dates[idx+1]:
                while stock < dates[idx+1]:
                    answer += 1
                    stock -= heapq.heappop(h)
    return answer