def solution(number, k):
    answer = ''
    start = 0
    while k > 0:
        for i in range(start, len(number)):
            if i == len(number)-1 and k > 0:
                return number[:len(number)-k]
            if number[i] < number[i+1]:
                number = number[:i] + number[i+1:]
                if i > 0:
                    start = i-1
                k -= 1
                break
            
    return number

print(solution("999999999", 8))


# stack으로 풀어보자


    