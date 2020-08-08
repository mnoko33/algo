def solution(s):
    N = len(s)
    answer = N
    for i in range(1, N):
        # i: 압축단위
        string = None
        cnt = 0
        temp_result = ''
        for j in range(0, N, i):
            target = s[j:j+i]
            if not string:
                string = target
                cnt = 1
                continue

            if string == target:
                cnt += 1
                continue

            if string != target:
                temp_result += (str(cnt) if cnt > 1 else '') + string
                string = target
                cnt = 1
                continue
        
        temp_result += (str(cnt) if cnt > 1 else '') + string
        answer = min(answer, len(temp_result))

    return answer


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))