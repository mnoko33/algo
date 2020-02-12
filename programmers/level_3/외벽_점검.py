###################################### deque는 왜 안될까 왜 틀릴까
# from collections import deque

# def solution(n, weak, dist):
#     D = len(dist)
#     answer = -1
#     Q = deque()
#     dist.sort(reverse=True)
#     Q.append([weak, dist])
#     while Q:
#         print('##################################################')
#         print('##################################################')
#         v = Q.popleft()
#         weak, dist = v[0], v[1]
#         print('weak :', weak)
#         print('dist :', dist)
#         for d in dist:
#             print('------------d = ' + str(d) + '---------------')
#             cnt = 100000
#             for i in range(len(weak)):
#                 new_weak = []
#                 for j in range(len(weak)):
#                     start = weak[i]
#                     target = weak[j]
#                     if start > target:
#                         target += n
#                     if target - start > d: # can not cover it 
#                         new_weak.append(weak[j])

#                 if not new_weak: # end!
#                     return D - len(dist) + 1
#                 if cnt < len(new_weak):
#                     continue
#                 else:
#                     cnt = min(len(new_weak), cnt)
#                 print('new_weak :', new_weak, " dist :", [x for x in dist if x != d])
#                 if new_weak == weak:
#                     continue
#                 Q.append([new_weak, [x for x in dist if x != d]])
#     return -1   



##################################### 시간초과
# def solution(n, weak, dist):
#     D = len(dist)
#     global answer
#     answer = 0xffff
    
#     def find(weak):
#         global answer
#         if not weak:
#             answer = D-len(dist)
#             return
#         if D-len(dist) >= answer:
#             return 
#         if not dist:
#             return
#         d = dist.pop(-1)
#         for i in range(len(weak)):
#             new_weak = []
#             for j in range(len(weak)):
#                 start = weak[i]
#                 target = weak[j]
#                 if start > target:
#                     target += n
#                 if target - start > d: # can not cover it 
#                     new_weak.append(weak[j])
#             if new_weak == weak:
#                 break
#             find(new_weak)
#         dist.append(d)
#     find(weak)    
#     if answer == 0xffff:
#         return -1
    
#     return answer

def DFS(weak, dist, n):
    global answer
    global D
    if not dist:
        return
    if not weak:
        return
    if answer > 0 and D - len(dist) >= answer:
        return
    # 배치할 친구 선택
    d = dist.pop(0)
    # 모든 결함에 친구들을 배치해본다
    N = len(weak)
    for i in range(N):
        # 친구를 배치를 하고 남은 결함
        new_weak = []
        for j in range(N):
            # 원형을 고려
            if weak[i] > weak[j]:
                if weak[j] + n - weak[i] > d:
                    new_weak.append(weak[j])
            else:
                if weak[j] - weak[i] > d:
                    new_weak.append(weak[j])

        # new_weak이 비어있다면 모든 결함을 커버한다는 의미
        if len(new_weak) == 0:
            if answer == -1:
                answer = D - len(dist) + 1
            else:
                answer = min(answer, D - len(dist))
            return
        # weak과 new_weak이 같다면 아무 것도 커버할 수 없기 때문에 stop
        if weak == new_weak:
            continue
        # 남은 외벽과 남은 친구들로 탐색 시행
        DFS(new_weak, [x for x in dist if x != d], n)
    
def solution(n, weak, dist):
    global answer
    global D
    dist.sort(reverse=True)
    answer = -1
    D = len(dist)
    DFS(weak, dist, n)
    return answer




print('answer > ')
print(solution( 50, [1, 5, 10, 12, 22, 25], [4, 3, 2, 1]))