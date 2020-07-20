def solution(board):
    def remove_if_possible(i,j, block):
        global cnt
        if i + 2 < N and board[i+2][j] == block:
            ni = i+2
            if j+1 < N and (board[i][j+1] == block or board[ni][j+1] == block or board[ni-1][j+1] == block):
                # 1-2, 2-2, 3-2
                nj = j+1
            else:
                # 1-4. 3-4
                nj = j-1
        elif i + 2 < N and j + 1 < N and board[i+2][j+1] == block:
            # 2-4
            ni, nj = i+2, j+1
        else:
            ni = i+1
            if j+2 < N and (board[i][j+2] == block or board[ni][j+2] == block):
                # 1-1, 1-3, 2-1, 3-3
                nj = j+2
            elif 0 <= j-2 and board[ni][j-2] == block:
                # 2-3
                nj = j-2
            else:
                if board[i+1][j] == block:
                    j-=1
                    nj = j + 2
        # check
        for x in range(i, ni+1):
            if j > nj:
                for y in range(nj, j+1):
                    if board[x][y] not in [block, '*']:
                        return
            else:
                for y in range(j, nj+1):
                    if board[x][y] not in [block, '*']:
                        return

        for x in range(i, ni+1):
            if j > nj:
                for y in range(nj, j+1):
                    board[x][y] = 0
            else:
                for y in range(j, nj+1):
                    board[x][y] = 0 
        cnt += 1
        return 
    
    N = len(board)
    global cnt
    cnt = 0
    print('########### original board ##########')
    for i in range(N):
        print([str(x) for x in board[i]])
    print()

    while True:
        xcnt = cnt
        visited = []
        # 1x1 블록 뿌리기
        for j in range(N):
            for i in range(N):
                if board[i][j] != 0:
                    if 0 <= i - 2:
                        board[i-2][j] = '*'
                    if 0 <= i - 1:
                        board[i-1][j] = '*'
                    break
        print('----------------------------------------------------------')
        print('>>>> 1x1 block')
        for i in range(N):
            print([str(x) for x in board[i]])
        print()

        # 없앨 수 있는 블룩 확인하고 없애기
        for i in range(N):
            for j in range(N):
                if board[i][j] not in [0, '*'] and board[i][j] not in visited:
                    block = board[i][j]
                    visited.append(block)
                    remove_if_possible(i,j,block)

        if xcnt == cnt:
            break

        # 미사용 1x1 블록 삭제
        for i in range(N):
            for j in range(N):
                if board[i][j] == '*':
                    board[i][j] = 0

        print('>>>> After Remove')
        for i in range(N):
            print([str(x) for x in board[i]])
        print()

    return cnt

boards = [
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0], [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5], [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]],
    [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,2,2,0,0,0,0,0],[0,0,0,2,1,0,0,0,0,0],[0,0,0,2,1,0,0,0,0,0], [0,0,0,0,1,1,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0]]
] 
answers = [
    2,1
]

for idx in range(len(boards)):
    v = solution(boards[idx])
    if v == answers[idx]:
        print(f'[성공] 실행한 결과값 {v}')
    else:
        print(f'[실패] 실행한 결과값 {v}이(가) 기대값 {answers[idx]}와(과) 다릅니다.')
