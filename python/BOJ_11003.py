# 최솟값 찾기

from collections import deque

def D(N, L, nums):
    def is_over_range(i):
        if not Q:
            return False
        idx, value = Q[0]
        return idx < i - L + 1
        
    def dequeue():
        Q.popleft()
        
    def enqueue(item):
        while Q and Q[-1][1] > item[1]:
            Q.pop()
        Q.append(item)
    
    Q = deque()
    min_table = []
    for idx, num in enumerate(nums):
        if is_over_range(idx):
            dequeue()
        enqueue([idx, num])
        min_table.append(str(Q[0][1]))
    return ' '.join(min_table)

N, L = map(int, input().split())
nums = list(map(int, input().split()))
print(D(N, L, nums))