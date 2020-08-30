def solution(s):
    answer = len(s)

    def compression(s, unit):
        acc = ''
        string = ''
        cnt = 0
        for i in range(0, len(s), unit):
            sub_s = s[i: i+unit]
            if not string:
                string = sub_s
                cnt = 1
                continue

            if string == sub_s:
                cnt += 1
            else:
                acc += f'{cnt}{string}' if cnt > 1 else string
                string = sub_s
                cnt = 1
        if string:
            acc += f'{cnt}{string}' if cnt > 1 else string
        acc += s[i+unit:]
        return acc
    
    for i in range(1, len(s) // 2 + 1):
        answer = min(answer, len(compression(s, i)))

    return answer


solution('ababcdcdababcdcd')