def solution(N, number):
    answer = 1
    possible = [[] for _ in range(8)]
    possible[0].append(N)
    while answer < 8:
        answer += 1
        tmp = possible[answer-1]
        for i in range(8):
            for j in range(i, 8):
                if i + j + 2 == answer:
                    for x in possible[i]:
                        for y in possible[j]:
                            tmp.append(x+y)
                            tmp.append(x*y)
                            if x != y:
                                tmp.append(x-y)
                                tmp.append(y-x)
                            if x != 0 and y != 0:
                                tmp.append(max(x,y)//min(x,y))
                            z = ''
                            for _ in range(answer):
                                z += f'{N}'
                            tmp.append(int(z))
        tmp = list(set(tmp))
        if number in tmp:
            return answer
    
    return - 1


print(solution(5, 12))