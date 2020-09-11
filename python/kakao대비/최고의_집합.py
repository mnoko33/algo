def solution(n, s):
    r, d = s // n, s % n
    if r == 0:
        return [-1]
    arr = [r] * n
    for i in range(d):
        arr[i] += 1
    return sorted(arr)