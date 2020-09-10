def solution(n, times):
    def is_treatable(N, temp_time):
        treatable_cnt = 0
        for time in times:
            treatable_cnt += temp_time // time
        return treatable_cnt >= N
    
    def bs(minv, maxv):
        if maxv - minv <= 1:
            return minv if is_treatable(n, minv) else maxv
        
        midv = (minv + maxv) // 2
        if is_treatable(n, midv):
            return bs(minv, midv)
        else:
            return bs(midv+1, maxv)

    minv = 0
    maxv = max(times) * n
    return bs(minv, maxv)


n = 6
times = [7, 10]
print(solution(n, times))