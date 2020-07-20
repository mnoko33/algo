N, L = list(map(int, input().split(' ')))
answer = ''
while L <= 100:
    target = N - L * (L-1) // 2
    if target % L == 0 and target // L >= 0:
        x = target // L
        for i in range(L):
            answer += str(x+i) + ' '
        print(answer[:-1])        
        break
    L += 1
if L > 100:
    print(-1)
