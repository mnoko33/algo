def solution(numbers):
    answer = []
    N = len(numbers)
    for i in range(N):
        for j in range(i+1, N):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))