import sys
sys.stdin = open('1655.txt', 'r')
# N = int(input())

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# class Classifier:
#     def __init__(self):
#         self.left = 0
#         self.right = 0
#         self.median = None

#     def insertNode(self, node):
#         if not self.median:
#             self.median = node
#         else:
#             target = self.median
            
#             if node.data <= target.data:
#                 self.left += 1
#                 while True:
#                     if not target.left:
#                         # None - node - target
#                         target.left = node
#                         node.right = target
#                         break
#                     if target.left.data <= node.data:
#                         # target.left - node - target
#                         target.left.right = node
#                         node.left = target.left
#                         target.left = node
#                         node.right = target
#                         break
#                     else:
#                         target = target.left
#             else:
#                 self.right += 1
#                 while True:    
#                     if not target.right:
#                         # target - node - None
#                         target.right = node
#                         node.left = target
#                         break
#                     if node.data < target.right.data:
#                         # target - node - target.right
#                         target.right.left = node
#                         node.right = target.right
#                         target.right = node
#                         node.left = target
#                         break
#                     else:
#                         target = target.right
#         # L L L M R R
#         if self.left > self.right:
#             self.median = self.median.left
#             self.left -= 1
#             self.right += 1
#         # L L M R R R R
#         if self.right - self.left == 2:
#             self.median = self.median.right
#             self.left += 1
#             self.right -= 1

#     def printMedian(self):
#         print(self.median.data)

# classfier = Classifier()
# for _ in range(N):
#     classfier.insertNode(Node(int(input())))
#     classfier.printMedian()

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
