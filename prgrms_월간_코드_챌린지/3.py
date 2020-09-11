import heapq

def solution(a):
    answer = 2
    left_side = [a[0]]
    right_side = a[2:]
    heapq.heapify(right_side)
    removed_right = []
    for i in range(1, len(a)-1):
        min_left = left_side[0]
        min_right = right_side[0]
        removed_right.append(a[i])
        if min_right in removed_right:
            while right_side:
                min_right = heapq.heappop(right_side)
                if min_right not in removed_right:
                    break

        print(min_left, a[i], min_right)
        if min_left > a[i] or min_right > a[i]:
            answer += 1
        heapq.heappush(left_side, a[i])
    return answer

a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
print(solution(a))