from collections import deque

def solution(n):
    result = 0
    Q = deque([[]])
    while Q:
        case = Q.popleft()
        for i in range(n):
            new_case = [x for x in case]
            if i in new_case:
                continue
            j = len(new_case)
            for x, y in enumerate(new_case):
                if abs(j-x) == abs(i-y):
                    break
            else:
                new_case.append(i)
                if len(new_case) == n:
                    print(new_case)
                    result += 1
                else:
                    Q.append(new_case)
    return result

n = 10
print(solution(n))
