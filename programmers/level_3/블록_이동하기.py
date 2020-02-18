from collections import deque

# def solution(board):
#     Q = deque()
#     Q.append([0, 0, 0, 1, 0])
#     N = len(board)
#     visit = [[0] * N for _ in range(N)]
#     visit[0][0] = 10000
#     target = [N-1,N-1]
#     while Q:
#         i1, j1, i2, j2, answer = Q.popleft()
#         answer += 1
#         # 가로일 떄
#         if i1 == i2:
#             # 오른쪽 이동
#             if j2 + 1 < N and board[i2][j2+1] == 0:
#                 if target == [i2,j2+1]:
#                     return answer
#                 if visit[i2][j2+1] == 0 or visit[i2][j2+1] > answer:
#                     Q.append([i2,j2,i2,j2+1,answer])
#                     visit[i2][j2+1] = answer
#             # 아래로 이동
#             if i1+1<N and i2+1<N and board[i1+1][j1] == 0 and board[i2+1][j2] == 0:
#                 if target == [i1+1,j1] or target == [i2+1,j2]:
#                     return answer
#                 if visit[i2+1][j2] == 0 or visit[i2+1][j2] > answer:
#                     Q.append([i1+1,j1,i2+1,j2,answer])
#                     Q.append([i2,j2,i2+1,j2,answer])
#                     visit[i2+1][j2] = answer
#                 if visit[i1+1][j1] == 0 or visit[i1+1][j1] > answer:
#                     Q.append([i1,j1,i1+1,j1,answer])
#                     visit[i1+1][j1] = answer
#             # 왼쪽이동
#             if 0<=j1-1 and board[i1][j1-1] == 0:
#                 if target == [i1,j1-1]:
#                     return answer
#                 if visit[i1][j1-1] == 0 or visit[i1][j1-1] > answer:
#                     Q.append([i1,j1-1,i1,j1,answer])
#                     visit[i1][j1-1] = answer
#             # 위로 이동
#             if 0<=i1-1 and 0<=i2-1 and board[i1-1][j1] == 0 and board[i2-1][j2] == 0:
#                 if target == [i1-1,j1] or target == [i2-1,j2]:
#                     return answer
#                 if visit[i1-1][j2] == 0 or visit[i1-1][j2] > answer:
#                     Q.append([i2-1,j2,i2,j2,answer])    
#                     Q.append([i1-1,j1,i2-1,j2,answer])
#                     visit[i1-1][j2] = answer
#                 if visit[i1-1][j1] == 0 or visit[i1-1][j1] > answer:
#                     Q.append([i1-1,j1,i1,j1,answer])
#                     visit[i1-1][j1] = answer
                
#         # 세로일 때
#         else:
#             # 오른쪽 이동, 우상, 우하
#             if j1 + 1 < N and j2 + 1 < N and board[i1][j1+1] == 0 and board[i2][j2+1] == 0:
#                 if target in [[i1,j1+1], [i2,j2+1]]:
#                     return answer
#                 if visit[i1][j1+1] == 0 or visit[i1][j1+1] > answer:
#                     visit[i1][j1+1] = answer
#                     Q.append([i1,j1,i1,j1+1,answer])
#                 if visit[i2][j2+1] == 0 or visit[i2][j2+1] > answer:
#                     visit[i2][j2+1] = answer
#                     Q.append([i1,j1+1,i2,j2+1,answer])
#                     Q.append([i2,j2,i2,j2+1,answer])
#             # 아래로 이동
#             if i2 + 1 < N and board[i2+1][j1] == 0:
#                 if target == [i2+1,j2]:
#                     return answer
#                 if visit[i2+1][j2] == 0 or visit[i2+1][j2] > answer:
#                     Q.append([i2,j2,i2+1,j2,answer])
#                     visit[i2+1][j2] = answer
#             # 왼쪽이동, 좌상, 좌하
#             if 0 <= j1 - 1 and 0 <= j2 - 1 and board[i1][j1-1] == 0 and board[i2][j2-1] == 0:
#                 if target in [[i1,j1-1], [i2,j2-1]]:
#                     return answer
#                 if visit[i2][j2-1] == 0 or visit[i2][j2-1] > answer:
#                     Q.append([i1,j2-1,i1,j1,answer])
#                     Q.append([i2,j2-1,i2,j2,answer])
#                     visit[i2][j2-1] = answer
#                 if visit[i1][j1-1] == 0 or visit[i1][j1-1] > answer:
#                     Q.append([i1,j1-1,i2,j2-1,answer])
#                     visit[i1][j1-1] = answer
                
#             # 위로 이동
#             if 0 <= i1 - 1 and board[i1-1][j1] == 0:
#                 if target == [i1-1,j1]:
#                     return answer
#                 if visit[i1-1][j1] == 0 or visit[i1-1][j1] > answer:
#                     visit[i1-1][j1] = answer
#                     Q.append([i1-1,j1,i1,j1,answer])
#     return answer

def solution(board):
    Q = deque()
    Q.append([0,0,0,1])
    N = len(board)
    visit = [[0] * N for _ in range(N)]
    visit[hy][hx] = 1
    visit[ty][tx] = 1
    target = [N-1,N-1]
    while Q:
        ty,tx,hy,hx = Q.popleft()
        # 가로일때
        if ty == hy:
            # right
            if hx+1 < N and board[hy][hx+1] == 0 and (visit[hy][hx+1] == 0 or visit[hy][hx+1] > visit[hy][hx]+1): 
                visit[hy][hx+1] = visit[hy][hx]+1
                Q.append([hy,hx,hy,hx+1])
            # down
            if hy+1 < N and board[hy+1][hx] == 0 and board[ty+1][tx] == 0 and 
        return 


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))


################################################################################################################################################
from collections import deque

def solution(board):
    answer = 0
    N = len(board)
    def check_boundary(coords):
        for coord in coords:
            if coord < 0 or coord >= N-1:
                return False
        return True
        
    # direction [down, right, left, up]
    dx = [1,0,0,-1]
    dy = [0,1,-1,0]
    Q = deque([[0,0,1]])
    while Q:
        x,y,d = Q.popleft()
        # 상하좌우 이동
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if d == 0:
                
            elif d == 1:
                
            elif d == 2:
                
            else:
                
    
    return answer