def solution(baseball):
    answer = 0
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                if i != j and j != k and i != k:
                    answer_cnt = 0

                    for n, s, b in baseball:
                        s_cnt = 0
                        b_cnt = 0
                        n = str(n)
                        if n[0] == str(i):
                            s_cnt += 1

                        if n[1] == str(j):
                            s_cnt += 1

                        if n[2] == str(k):
                            s_cnt += 1

                        if str(i) in n:
                            b_cnt += 1
                        if str(j) in n:
                            b_cnt += 1
                        if str(k) in n:
                            b_cnt += 1
                        b_cnt -= s_cnt

                        if s == s_cnt and b == b_cnt:
                            answer_cnt += 1
                    if answer_cnt == len(baseball):
                        answer += 1

    return answer