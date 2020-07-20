import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while True:
        if len(scoville) >= 2:
            tmp = 0
            cnt += 1
            tmp += heapq.heappop(scoville)
            tmp += heapq.heappop(scoville) * 2
            heapq.heappush(scoville, tmp)
            if scoville[0] >= K:
                return cnt
        else:
            return -1