def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    food_times = [[food_time, idx+1] for idx, food_time in enumerate(food_times)]
    food_times.sort(key=lambda x: x[0])

    remove_cnt = 0
    plates_cnt = len(food_times)
    idx = 0
    while True:
        minv = food_times[idx][0] - remove_cnt
        if minv * plates_cnt < k:
            k -= minv * plates_cnt
            plates_cnt -= 1
            remove_cnt += minv
            idx += 1
        else:
            break
    
    food_times = food_times[idx:]
    food_times.sort(key=lambda x: x[1])
    return food_times[k%plates_cnt][1]

food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))