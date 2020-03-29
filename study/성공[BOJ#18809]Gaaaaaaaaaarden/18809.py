import sys
sys.stdin = open('18809.txt', 'r')
from collections import deque
from itertools import combinations

global N
N, M, G, R = map(int, input().split())
garden = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 0: 호수
# 1: 배양액 x
# 2: 배양액 o
# 3: 빨간 배양액
# 4: 초록 배양액
def get_flower(G_list, R_list):
    temp_answer = 0
    global N
    # temp_garden 
    Q = deque()
    # init
    for r in R_list:
        x,y = r[0],r[1]
        temp_garden[x][y] = [0,3]
        Q.append((0,'r',x,y))
    for g in G_list:
        x,y = g[0],g[1]
        temp_garden[x][y] = [0,4]
        Q.append((0,'g',x,y))
    while Q:
        cost, color, x, y = Q.popleft()
        if temp_garden[x][y][1] == -1:
            continue
        cost += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 경계 체크 
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            # 퍼질 수 있는 곳일 때
            if temp_garden[nx][ny][1] == 1 or temp_garden[nx][ny][1] == 2:
                if color == 'r':
                    temp_garden[nx][ny] = [cost, 3]
                else:
                    temp_garden[nx][ny] = [cost, 4]
                Q.append((cost, color, nx, ny))
                continue
            # 꽃이 필 수 있는 곳일 때
            if color == 'r' and temp_garden[nx][ny][1] == 4 and temp_garden[nx][ny][0] == cost:
                temp_answer += 1
                temp_garden[nx][ny][1] = -1 # 꽃
                continue
            if color == 'g' and temp_garden[nx][ny][1] == 3 and temp_garden[nx][ny][0] == cost:
                temp_answer += 1
                temp_garden[nx][ny][1] = -1 # 꽃
                continue
    return temp_answer

def find_possible_area():
    possible = []
    for i in range(N):
        for j in range(M):
            if garden[i][j] == 2:
                possible.append([i, j])
    return possible

answer = 0

# 배양액을 뿌릴 수 있는 곳
possible = find_possible_area()
# possible idx list
P = [i for i in range(len(possible))]
# 전체 조합
RG_comb = list(combinations(P, R+G))
for rg_comb in RG_comb:
    # rg_comb => R+G개의 index
    G_comb = list(combinations(rg_comb, G))
    for g_comb in G_comb:
        r_comb = []
        for v in rg_comb:
            if v not in g_comb:
                r_comb.append(v)
        G_list = [possible[i] for i in g_comb]
        R_list = [possible[i] for i in r_comb]
        # temp_garden 초기화
        temp_garden = [[[0, 0] for _ in range(M)] for _ in range(N)]
        for i in range(N):
            for j in range(M):
                temp_garden[i][j][1] = garden[i][j]
        answer = max(get_flower(G_list, R_list), answer)
print(answer)