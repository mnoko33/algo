import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    H = []
    cnt_plates = len(food_times)
    cnt_removed = 0
    for idx, food_time in enumerate(food_times):
        heapq.heappush(H, (food_time, idx+1))
    while True:
        x = H[0]
        if k > (x[0] - cnt_removed) * cnt_plates:
            x = heapq.heappop(H)
            k -= (x[0] - cnt_removed) * cnt_plates
            cnt_removed = x[0]
            cnt_plates -= 1
        else:
            break
    H = sorted(H, key=lambda x: x[1])
    return H[k%cnt_plates][1]