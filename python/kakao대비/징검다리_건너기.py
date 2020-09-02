def solution(stones, k):
    # n명의 니니즈 친구들이 돌다리를 건널 수 있는지
    def is_possible(n, k):
        # n - 1명이 건너고 난 후 1개 이상인 돌들의 idx
        remain_stones = [0]
        for idx, stone in enumerate(stones):
            if stone > n-1:
                remain_stones.append(idx+1)
        remain_stones.append(len(stones)+1)
        
        for i in range(len(remain_stones)-1):
            stone_idx = remain_stones[i]
            next_stone_idx = remain_stones[i+1]
            if next_stone_idx - stone_idx > k:
                return False
        return True

    def binary_search(minv, maxv):
        if maxv - minv <= 1:
            return maxv if is_possible(maxv, k) else minv

        midv = (minv + maxv) // 2
        if is_possible(midv, k):
            return binary_search(midv, maxv)
        else:
            return binary_search(minv, midv-1)

    return binary_search(0, max(stones))

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))