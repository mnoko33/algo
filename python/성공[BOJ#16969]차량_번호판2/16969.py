import sys
sys.stdin = open('16969.txt', 'r')

answer = 1
before = -1
for cd in input():
    if before == -1:
        if cd == 'c':
            answer *= 26
            before = 'c'
        else:
            answer *= 10
            before = 'd'
    else:
        # 문자일 때
        if cd == 'c':
            if before == 'c':
                answer *= 25
            else:
                answer *= 26
                before = 'c'
        # 숫자일 때
        else:
            if before == cd:
                answer *= 9
            else:
                answer *= 10
                before = 'd'
    answer %= 1000000009
print(answer)