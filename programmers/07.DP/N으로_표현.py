def solution(N, number):
    answer = 1
    possible = [N]
    while answer <= 8:
        answer += 1
        tmp = []
        for p in possible:
            tmp.append(p+N)
            tmp.append(p*N)
            if not N == p:
                tmp.append(p-N)
                tmp.append(N-p)
            if N != 0 and p != 0:
                tmp.append(max(p,N) // min(p,N))
            tmp.append(int(str(N)*answer))

        tmp = list(set(tmp))
        if number in tmp:
            return answer
        possible = tmp
    return -1

print(solution(5, 12))