import math
from collections import deque

def get_sqrt(N):
    sqrt = math.sqrt(N)
    if int(sqrt) == sqrt:
        return int(sqrt)
    else:
        return int(sqrt) + 1

def is_prime(N):
    for i in range(2, get_sqrt(N)+1):
        if N % i == 0:
            return False
    return True

def main(A, B):
    if A == B:
        return 0
    visited = [0] * 9000
    Q = deque()
    Q.append([A, 0])
    while Q:
        num, cnt = Q.popleft()
        if num == B:
            return cnt
        for i in range(4):
            for j in range(10):
                if i == 0 and j == 0:
                    continue
                if str(num)[i] == j:
                    continue
                nums = [x for x in str(num)]
                nums[i] = str(j)
                new_num = int(''.join(nums))
                if visited[new_num-1000]:
                    continue
                visited[new_num-1000] = 1
                if is_prime(new_num):
                    Q.append([new_num, cnt + 1])
    return 'impossible'
        
N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    print(main(A, B))