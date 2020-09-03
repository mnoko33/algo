from collections import deque

def solution(n, weak, dist):
    dist.sort(reverse=True)
    N = len(dist)
    Q = deque([
        [[x for x in weak], [y for y in dist]]
    ])
    answer = -1
    while Q:
        weak, dist = Q.popleft()
        friend = dist.pop(0)

        removed_cnt = 0
        will_be_removed = []

        for i, wp in enumerate(weak):
            new_weak = weak[i:] + [x+n for x in weak[:i]]
            cover = wp + friend
            removed = []
            for new_wp in new_weak:
                if new_wp <= cover:
                    removed.append(new_wp%n)
                else:
                    break
            
            if len(removed) == removed_cnt:
                will_be_removed.append(removed)
                continue
                
            if len(removed) > removed_cnt:
                removed_cnt = len(removed)
                will_be_removed = [removed]

        if len(weak) == removed_cnt:
            return N - len(dist)
            answer = min(answer, N - len(dist)) if answer >= 0 else N - len(dist)
            continue

        if not dist:
            continue

        # 제거되는 weak이 없다면 더 이상 볼 필요 없는 경우
        if removed_cnt == 0:
            continue

        for removed in will_be_removed:
            Q.append([sorted([x for x in weak if x not in removed]), [y for y in dist]])

    return answer

n = 200
weak = [0, 10, 50, 80, 120, 160]
dist = [1, 10, 5, 40, 30]
print(solution(n, weak, dist))

