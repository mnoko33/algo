def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    acc = 0

    for x, y in zip(A, B):
        acc += x * y

    return acc


print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1, 2], [3, 4]))