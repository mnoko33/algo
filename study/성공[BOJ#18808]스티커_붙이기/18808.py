import sys
sys.stdin = open('18808.txt', 'r')

def rotate(sticker,R,C):
    new_sticker = [[0] * R for _ in range(C)]
    for r in range(R):
        for c in range(C):
            new_sticker[c][R-1-r] = sticker[r][c]
    return new_sticker

def find_possible(arr, i,j,R,C,H,W):
    if R+i > H or C+j > W:
        return False
    for r in range(R):
        for c in range(C):
            if notebook[r+i][c+j] == 1 and arr[r][c] == 1:
                return False
    return True

def add_sticker(arr, i,j,R,C):
    for r in range(R):
        for c in range(C):
            notebook[r+i][c+j] += arr[r][c]

H, W, K = map(int, input().split(' '))
notebook = [[0] * W for _ in range(H)]
for _ in range(K):
    R,C = map(int, input().split(' '))
    sticker = [list(map(int, input().split(' '))) for _ in range(R)]
    # 탐색해보고 안되면 회전
    flag = False
    for _ in range(4):
        R = len(sticker)
        C = len(sticker[0])
        for i in range(H):
            for j in range(W):
                # (i, j)에서 붙일 수 있는지 체크
                if find_possible(sticker, i,j,R,C,H,W):
                    add_sticker(sticker, i,j,R,C)
                    flag = True
                    break
            if flag == True:
                break
        if flag == True:
            break
        else:
            sticker = rotate(sticker,R,C)

answer = 0
for i in range(H):
    for j in range(W):
        if notebook[i][j] == 1:
            answer += 1
print(answer)
