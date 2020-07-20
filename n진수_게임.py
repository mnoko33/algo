def solution(n, t, m, p):
    answer = ''
    cnt = t * m
    num = 0
    tmp_answer = ''
    convert = [str(i) for i in range(10)] + ["A", "B", "C", "D", "E", "F"]
    while cnt > 0:
        tmp = ''
        tmp_num = num
        while True:
            b = tmp_num % n
            tmp_num = tmp_num // n
            if tmp_num > 0:
                tmp = convert[b] + tmp                
            else:
                tmp = convert[b] + tmp
                break
                
        tmp_answer += tmp
        cnt -= len(tmp)
        num += 1

    for i in range(t):
        answer += tmp_answer[p + m * i - 1]
    
    return answer