def solution(m, n, board):
    removed = []
    answer = 0
    # make it to list
    for i in range(m):
        board[i] = [x for x in board[i]]

    while True:
        for i in range(m):
            for j in range(n):
                if i == m-1 or j == n-1:
                    continue
                block = board[i][j]
                if block == 'X':
                    continue
                if (board[i+1][j] == block) and (board[i][j+1] == block) and (board[i+1][j+1] == block):
                    for t in [[i,j],[i+1,j],[i,j+1],[i+1,j+1]]:
                        if t not in removed:
                            removed.append(t)
        if removed == []:
            break

        # remove target
        for i,j in removed:
            board[i][j] = 'X'
            answer += 1
        removed = []
        
        for j in range(n):
            for i in range(m):
                i = m-i-1
                if i>0 and board[i][j] == "X":
                    tmp = i
                    while tmp > 0:
                        tmp -= 1
                        if board[tmp][j] != "X":
                            board[i][j], board[tmp][j] = board[tmp][j], board[i][j]
                            break
        
    return answer

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))