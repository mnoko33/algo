import sys
sys.stdin = open('1799.txt', 'r')

global N
N = int(input())
chess = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 1, -1, -1]
dy = [1, -1, 1, -1]

# 해당 위치에 비숍을 둘 수 있는지를 체크
def check(x,y):
    global N
    if chess[x][y] == 0:
        return False
    for d in range(4):
        i = 1
        while True:
            nx = x + dx[d] * i
            ny = y + dy[d] * i
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                break
            # 이미 비숍이 놓여져있을 경우
            if chess[nx][ny] == 9:
                return False
            i += 1
    return True

# 해당 위치에서부터 탐색을 시작
def search(x,y, isTwice):
    global N
    global cnt
    global answer
    if x == N:
        answer = max(answer, cnt)
        return 

    # 다음 탐색 위치
    # 짝수일 때
    if y % 2 == 0:
        if y + 2 >= N:
            ny = 1
            nx = x+1
        else:
            ny = y+2
            nx = x
    else:
        if y + 2 >= N:
            ny = 0
            nx = x + 1
        else:
            ny = y+2
            nx = x
    
    # 해당 위치에 둘 수 있을 때
    if check(x,y):
        # 안두고 패스
        search(nx,ny,isTwice)
        # 채스 두기
        chess[x][y] = 9
        cnt += 1
        search(nx,ny,isTwice)
        chess[x][y] = 1
        cnt -= 1
    else:
        search(nx,ny,isTwice)

global answer
global temp_answer
global cnt
answer = 0
cnt = 0
search(0,0, False)

# 기존 결과값을 저장하고 초기화
temp_answer = answer
answer = 0
cnt = 0
search(0,1, True)

print(answer + temp_answer)