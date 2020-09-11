def solution(numbers):
    N = len(numbers)
    result = []
    for i in range(N):
        for j in range(N):
            if i != j:
                result.append(numbers[i]+numbers[j])
    result = list(set(result))
    result.sort()
    return result