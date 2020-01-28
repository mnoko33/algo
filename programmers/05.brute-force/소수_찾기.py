import itertools

def solution(numbers):
    answer = 0
    numbers = [num for num in numbers]
    candidate = []
    for i in range(1, len(numbers)+1):
        perms = list(itertools.permutations(numbers, i))
        for perm in perms:
            tmp_s = ''
            for s in perm:
                tmp_s += s
            candidate.append(int(tmp_s))
    candidate = list(set(candidate))

    def check_is_sosu(n):
        if n in [0, 1]:
            return False

        s = 2
        e = int(n ** 0.5)
        for i in range(s, e+1):
            if n % i == 0:
                return False
        return True

    for _candidate in candidate:
        if check_is_sosu(_candidate):
            answer += 1

    return answer