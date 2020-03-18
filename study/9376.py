import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('9376.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x,y):
    global flag, answer, door_cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 탈출 성공
        if nx < 0 or ny < 0 or nx >= h or ny >= w:
            if flag == True:
                answer = min(door_cnt, answer)
                return
            else:
                return
        # 위치
        target = jail[nx][ny]
        # 이미 방문한 곳일 때
        # if target == True:
        #     continue
        # 다른 죄수일 때
        if target == '$':
            flag = True
            # jail[nx][ny] = True
            dfs(nx, ny)
            # jail[nx][ny] = '$'
            flag = False
            continue
        # 벽
        if target == '*':
            continue
        # 빈 공간
        if target == '.':
            # jail[nx][ny] = True
            dfs(nx, ny)
            # jail[nx][ny] = '.'
            continue
        # 문
        if target == '#':
            # 가지치기
            if door_cnt + 1 >= answer:
                return
            jail[nx][ny] = True
            door_cnt += 1
            dfs(nx, ny)
            jail[nx][ny] = '#'
            door_cnt -= 1
            continue


for _ in range(int(input())):
    h,w = map(int, input().split(' '))
    jail = [[x for x in input()] for _ in range(h)]
    # 죄수 위치
    prisoner = []
    for i in range(h):
        for j in range(w):
            if jail[i][j] == '$':
                prisoner.append((i, j))
    p1 = prisoner[0]
    p2 = prisoner[1]
    # 죄수 2명인가?
    global flag, answer, door_cnt
    flag = False
    answer = 0xffff
    # door cnt
    door_cnt = 0
    print('--')
    dfs(p1[0], p1[1])
    print(answer)
    