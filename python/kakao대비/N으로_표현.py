def solution(N, target):
    result = [[] for _ in range(9)]

    # 초기값 세팅
    result[1] = [N]
    if target == N:
        return 1

    for cnt in range(2, 9):
        self_num = int(str(N) * cnt)
        if self_num == target:
            return cnt
        result[cnt].append(self_num)
        for i in range(1, cnt//2+1):
            x, y = i, cnt-i
            for num1 in result[x]:
                for num2 in result[y]:
                    temp = [num1+num2, num1-num2, num2-num1, num1*num2]
                    if num1:
                        temp.append(num2//num1)
                    if num2:
                        temp.append(num1//num2)
                    if target in temp:
                        return cnt
                    result[cnt] += temp
                    result[cnt] = list(set(result[cnt]))

    return -1