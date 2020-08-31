def solution(n, t, m, p):
    def convert_int_to_alpha(n):
        if n == '10':
            return 'A'
        if n == '11':
            return 'B'
        if n == '12':
            return 'C'
        if n == '13':
            return 'D'
        if n == '14':
            return 'E'
        if n == '15':
            return 'F'
        return n

    def get_next_notaion(num, n):
        idx = len(num) - 1
        while True:
            new_num = int(num[idx]) + 1
            # +1한 숫자가 n보다 크거나 같을 경우
            if new_num >= n:
                num[idx] = '0'
                idx -= 1
                if idx < 0:
                    return ['1'] + num
            else:
                num[idx] = str(new_num)
                break
        return num

    result = ['0']
    cnt = t * m
    num = ['0']
    while cnt >= len(result):
        num = get_next_notaion(num, n)
        result += num

    answer = ''
    for i in range(t):
        answer += convert_int_to_alpha(result[i * m + p - 1])

    return answer

n = 16
t = 16
m = 2
p = 1
print(solution(n, t, m, p))

