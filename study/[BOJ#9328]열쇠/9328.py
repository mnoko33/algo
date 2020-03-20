import sys
sys.stdin = open('9328.txt', 'r')
from collections import deque

for _ in range(int(input())):
    h,w = map(int, input().split(' '))
    building = []
    # 가장자리에 길이 있는 지도 그리기 
    building.append(['.'] * (w+2))
    for _ in range(h):
        building.append(['.'] + [x for x in input()] + ['.'])
    building.append(['.'] * (w+2))
    # 열쇠 꾸러미
    temp = input()
    if temp == '0':
        keys = []
    else:
        keys = [key for key in temp]
    # 큐 생성
    Q = deque()
    # 출발점 (0, 0)
    Q.append((0, 0))
    building[0][0] = True
    # 4방향 탐색
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    # 문서의 갯수
    documents = 0
    # 방문했는데 열지 못한 문
    doors = {}
    iii=0
    while Q:
        # print('out Q')
        while Q:
            iii += 1
            x,y = Q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 경계
                if nx < 0 or ny < 0 or nx >= h+2 or ny >= w+2:
                    continue
                now = building[nx][ny]
                # 벽
                if now == '*':
                    continue
                # 이미 방문한 곳
                if now == True:
                    continue
                # 통로
                if now == '.':
                    Q.append((nx, ny))
                    building[nx][ny] = True
                    continue
                # 문
                if 65 <= ord(now) and ord(now) <= 90:
                    # 열쇠가 있을 때
                    if now.lower() in keys:
                        building[nx][ny] = True
                        Q.append((nx, ny))
                    else:
                        # 이미 문이 등록
                        if now in doors.keys():
                            doors[now].append((nx, ny))
                            building[nx][ny] = True
                        else:
                            doors[now] = [(nx, ny)]
                    continue
                # 열쇠
                if 97 <= ord(now) and ord(now) <= 122:
                    keys.append(now)
                    building[nx][ny] = True
                    Q.append((nx, ny))
                    continue
                # 문서
                if now == '$':
                    documents += 1
                    building[nx][ny] = True
                    Q.append((nx, ny))
        # 못열어본 방문이 있을 경우
        if len(doors) > 0:    
            # 해당 문을 열 수 있는 열쇠가 있는지 체크
            for key in keys:
                if key.upper() in doors:
                    for coord in doors[key.upper()]:
                        Q.append(coord)
                    del doors[key.upper()]
    print(documents)
