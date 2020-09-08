def solution(board, moves):
    def rotate_board(board):
        N = len(board)
        new_board = [[] for _ in range(N)]
        for i in range(N):
            for j in range(N-1, -1, -1):
                box = board[j][i]
                if box > 0:
                    new_board[i].append(box)
                else:
                    break
        return new_board
    
    board = rotate_board(board)
    answer = 0
    selected_stack = []
    for move in moves:
        if not board[move-1]:
            continue
        selected_doll = board[move-1].pop()
        if not selected_stack:
            selected_stack.append(selected_doll) 
        elif selected_stack[-1] == selected_doll:
            selected_stack.pop()
            answer += 2
        else:
            selected_stack.append(selected_doll)
    return answer


board = []
moves = []
print(solution(board, moves))