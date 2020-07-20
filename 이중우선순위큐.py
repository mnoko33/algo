# def solution(operations):
#     answer = []
#     for operation in operations:
#         order, v = operation.split(' ')
#         if order == 'I':
#             answer.append(int(v))
#         else:
#             if v == '1' and answer:
#                 answer.remove(max(answer))
#             elif v == '-1' and answer:
#                 answer.remove(min(answer))
#     if not answer:
#         answer.append(0)
#     return [max(answer), min(answer)]


# 힙을 사용해서 풀어보자

import heapq

def solution(operations):
    max_h = []
    min_h = []
    idxs = []
    idx = 0
    for operation in operations:
        order, num = operation.split(' ')
        if order == "I":
            heapq.heappush(max_h, (-int(num), idx))
            heapq.heappush(min_h, (int(num), idx))
            idx += 1
        else:
            if num == '1':
                while max_h:
                    (num, i) = heapq.heappop(max_h)
                    if i not in idxs:
                        idxs.append(i)
                        break
            else:
                while min_h:
                    (num, i) = heapq.heappop(min_h)
                    if i not in idxs:
                        idxs.append(i)
                        break
    max_v = 0
    min_v = 0
    while max_h:
        v, idx = heapq.heappop(max_h)
        if idx not in idxs:
            max_v = -v
            break
    while min_h:
        v, idx = heapq.heappop(min_h)
        if idx not in idxs:
            min_v = v
            break
    return [max_v, min_v]

print(solution(	["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))