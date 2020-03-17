import sys
sys.stdin = open('9328.txt', 'r')
from collections import deque

def is_entry(x,y):
    target = building[x][y]
    if target == '*':
        return False
    if target in ['.', '$']:
        return True
    if target.islower():
        return True
    if target.isupper() and target.lower() in key_set:
        return True
    return False
    

def check_edge():
    entry = []
    # 가로
    for i in range(w):
        if is_entry(0, i):
            entry.append((0, i))
        if is_entry(h-1, i):
            entry.append((h-1, i))
    # 세로
    for j in range(1, h-1):
        if is_entry(j, 0):
            entry.append((j, 0))
        if is_entry(j, w-1):
            entry.append((j, w-1))
    return entry

for test_case in range(int(input())):
    h,w = map(int, input().split(' '))
    building = [[x for x in input()] for _ in range(h)]
    temp = input()
    key_set = [] if temp == '0' else [x for x in temp]
    new_key = []
    answer = 0
    Q = deque()
    # 입구
    entry = check_edge()
    if not entry:
        print(0)
        continue
    for i,j in entry:
        # 그냥 길
        if building[i][j] == '.':
            building[i][j] = True
        # 문서 줍줍
        elif building[i][j] == '$':
            building[i][j] = True
            answer += 1
        # 키 줍줍    
        elif building[i][j].islower():
            key_set.append(building[i][j])
            building[i][j] = True
        # key가 있는 문
        else:
            building[i][j] = True
        Q.append((i,j))
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    door = []
    while Q:
        while Q:
            v = Q.popleft()
            for i in range(4):
                nx, ny = v[0] + dx[i], v[1] + dy[i]
                # 경계 체크
                if nx < 0 or ny < 0 or nx >= h or ny >= w:
                    continue
                if building[nx][ny] == True:
                    continue
                # 통로 
                if building[nx][ny] == '.':
                    building[nx][ny] = True
                    Q.append((nx, ny))
                    continue
                # 문서 줍줍
                if building[nx][ny] == '$':
                    answer += 1
                    building[nx][ny] = True
                    Q.append((nx, ny))
                    continue
                # 키 줍줍
                if building[nx][ny] not in ['*', True] and building[nx][ny].islower():
                    new_key.append(building[nx][ny])
                    Q.append((nx, ny))
                    continue
                # 문일 때
                if building[nx][ny] not in ['*', True] and building[nx][ny].isupper():
                    # 열 수 있는 문
                    if building[nx][ny].lower() in key_set:
                        building[nx][ny] = True
                        Q.append((nx, ny))
                    # 열 수 없는 문
                    else:
                        if (nx, ny, building[nx][ny]) not in door:
                            door.append((nx, ny, building[nx][ny]))
                        building[nx][ny] = True
                
        if not new_key:
            break
        else:
            left_door = []
            for x,y,char in door:
                if char.lower() in new_key:
                    Q.append((x,y))
                else:
                    left_door.append((x,y,char))
            key_set += new_key
            key_set = list(set(key_set))
            door = left_door
            new_key = []
    print(answer)
    # break