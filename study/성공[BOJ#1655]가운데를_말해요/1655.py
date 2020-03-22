import sys
sys.stdin = open('1655.txt', 'r')

import heapq
N = int(input())
maxH = []
minH = []
# maxH < num < minH
for _ in range(N):
    if len(maxH) == len(minH):
        heapq.heappush(maxH, -1 * int(input()))
    else:
        heapq.heappush(minH, int(input()))
    if minH and -1 * maxH[0] > minH[0]:
        max_in_maxH = heapq.heappop(maxH)
        min_in_minH = heapq.heappop(minH)
        heapq.heappush(maxH, min_in_minH * -1)
        heapq.heappush(minH, max_in_maxH * -1)
    
    print(-1 * maxH[0])
