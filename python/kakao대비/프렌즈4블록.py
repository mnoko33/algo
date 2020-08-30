from collections import deque

def solution(R, C, board):
    board = list(map(lambda x: [s for s in x], board))
    global answer
    answer = 0
    def get_removable(r, c):
        def check_boundary():
            return r + 1 < R and c + 1 < C
    
        def check_right():
            return board[r][c+1] == block

        def check_under():
            return board[r+1][c] == block

        def check_diagonal():
            return board[r+1][c+1] == block

        block = board[r][c]
        if check_boundary() and check_right() and check_under() and check_diagonal():
            return [(r, c), (r+1, c), (r, c+1), (r+1, c+1)]
        else:
            return [] 


    def remove_block(block_list):
        global answer

        for r, c in block_list:
            board[r][c] = 0
            answer += 1

    def apply_gravity():
        def apply_gravity_col(c):
            def get_stack(c):
                stack = []
                for r in range(R):
                    block = board[r][c]
                    if block:
                        stack.append(block)
                return stack
            
            def set_col_vacant(c):
                for r in range(R):
                    board[r][c] = 0

            block_stack = get_stack(c)
            set_col_vacant(c)
            for r in range(R - 1, -1, -1):
                if not block_stack:
                    return
                board[r][c] = block_stack.pop()

        for c in range(C):
            apply_gravity_col(c)

    while True:
        removable_block_list = []
        for r in range(R):
            for c in range(C):
                if board[r][c]:
                    removable_block_list += get_removable(r, c)

        remove_block(list(set(removable_block_list)))
        if not removable_block_list:
            return answer
        apply_gravity()

m = 4
n = 5
board = ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']
print(solution(m, n, board))


