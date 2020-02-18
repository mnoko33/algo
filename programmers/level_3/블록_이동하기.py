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

# def solution(board):
#     Q = deque()
#     Q.append([0,0,0,1])
#     N = len(board)
#     visit = [[0] * N for _ in range(N)]
#     visit[hy][hx] = 1
#     visit[ty][tx] = 1
#     target = [N-1,N-1]
#     while Q:
#         ty,tx,hy,hx = Q.popleft()
#         # 가로일때
#         if ty == hy:
#             # right
#             if hx+1 < N and board[hy][hx+1] == 0 and (visit[hy][hx+1] == 0 or visit[hy][hx+1] > visit[hy][hx]+1): 
#                 visit[hy][hx+1] = visit[hy][hx]+1
#                 Q.append([hy,hx,hy,hx+1])
#             # down
#             if hy+1 < N and board[hy+1][hx] == 0 and board[ty+1][tx] == 0 and 
#         return 


# print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))


################################################################################################################################################
from collections import deque

def solution(board):
    answer = 0
    N = len(board)        
    # direction [down, right, left, up]
    visit = [[0] * N for _ in range(N)]
    visit[0][0] = 1
    visit[0][1] = 1
    dx = [1,0,0,-1]
    dy = [0,1,-1,0]
    Q = deque([[0,0,1,0]])
    while Q:
        print('===================')
        print(Q)
        for _visit in visit:
            print(_visit)
        x,y,d,ans = Q.popleft()
        xx, yy = x+dx[d],y+dy[d]
        ans+=1
        # 상하좌우 이동
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            nxx,nyy = xx+dx[i],yy+dy[i]
            if 0 <= nx and 0 <= ny and 0 <= nxx and 0 <= nyy and nx < N and ny < N and nxx < N and nyy < N and board[nx][ny] == 0 and board[nxx][nyy] == 0:
                if (nx==N-1 and ny==N-1) or (nxx==N-1 and nyy==N-1):
                    return ans
                if visit[nx][ny] == 0 or visit[nxx][nyy] == 0 or visit[nx][ny] > ans or visit[nxx][nyy] > ans:
                    visit[nx][ny] = ans
                    visit[nxx][nyy] = ans
                    Q.append([nx,ny,d,ans])
        #대각선이동
        xx, yy = x + dx[d], y + dy[d]
        if d == 1 or d == 2:
            # 아래체크
            if x+1 < N and xx+1 < N and board[x+1][y] == 0 and board[xx+1][yy] == 0:
                if (x+1==N-1 and y==N-1) or (xx+1==N-1 and yy==N-1):
                    return ans
                if visit[x+1][y] == 0 or visit[x+1][y] >= ans:
                    visit[x+1][y] = ans
                    Q.append([x,y,0,ans])
                if visit[xx+1][yy] == 0 or visit[xx+1][yy] >= ans:
                    visit[xx+1][yy] = ans
                    Q.append([xx,yy,0,ans])
            # 위체크
            if 0<=x-1 and 0<=xx-1 and board[x-1][y] == 0 and board[xx-1][yy] == 0:
                if (x-1==N-1 and y==N-1) or (xx-1==N-1 and yy==N-1):
                    return ans
                if visit[x-1][y] == 0 or visit[x-1][y] >= ans:
                    visit[x-1][y] = ans
                    Q.append([x,y,3,ans])
                if visit[xx-1][yy] == 0 or visit[xx-1][yy] >= ans:
                    visit[xx-1][yy] = ans
                    Q.append([xx,yy,3,ans])
        if d ==0 or d == 3:
            # 오른쪽체크
            if y+1<N and yy+1<N and board[x][y+1] == 0 and board[xx][yy+1] == 0:
                if (x==N-1 and y+1==N-1) or (xx==N-1 and yy+1==N-1):
                    return ans
                if visit[x][y+1] == 0 or visit[x][y+1] >= ans:
                    visit[x][y+1] = ans
                    Q.append([x,y,1,ans])
                if visit[xx][yy+1] == 0 or visit[xx][yy+1] >= ans:
                    visit[xx][yy+1] = ans
                    Q.append([xx,yy,1,ans])
            # 왼쪽체크
            if 0<=y-1 and 0<=yy-1 and board[x][y-1] == 0 and board[xx][yy-1] == 0:
                if (x==N-1 and y-1==N-1) or (xx==N-1 and yy-1==N-1):
                    return ans
                if visit[x][y-1] == 0 or visit[x][y-1] >= ans:
                    visit[x][y-1] = ans
                    Q.append([x,y,2,ans])
                if visit[xx][yy-1] == 0 or visit[xx][yy-1] >= ans:
                    visit[xx][yy-1] = ans
                    Q.append([xx,yy,2,ans])
        
    return answer

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))