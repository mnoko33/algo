from collections import deque

def solution(board):
    answer = 0
    N = len(board)        
    # direction [down, right, left, up]
    visit = [[[0,0] for _ in range(N)] for _ in range(N)] # [가로, 세로]
    visit[0][0][0] = 1
    visit[0][1][0] = 1
    dx = [1,0,0,-1]
    dy = [0,1,-1,0]
    Q = deque([[0,0,1,0]])
    while Q:
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
                if d == 1 or d == 2:
                    if visit[nx][ny][0] == 0 or visit[nxx][nyy][0] == 0 or visit[nx][ny][0] > ans or visit[nxx][nyy][0] > ans:
                        visit[nx][ny][0] = ans
                        visit[nxx][nyy][0] = ans
                        Q.append([nx,ny,d,ans])
                elif d == 0 or d == 3:
                    if visit[nx][ny][1] == 0 or visit[nxx][nyy][1] == 0 or visit[nx][ny][1] > ans or visit[nxx][nyy][1] > ans:
                        visit[nx][ny][1] = ans
                        visit[nxx][nyy][1] = ans
                        Q.append([nx,ny,d,ans])
                        
        #대각선이동
        xx, yy = x + dx[d], y + dy[d]
        if d == 1 or d == 2:
            # 아래체크
            if x+1 < N and xx+1 < N and board[x+1][y] == 0 and board[xx+1][yy] == 0:
                if (x+1==N-1 and y==N-1) or (xx+1==N-1 and yy==N-1):
                    return ans
                if visit[x+1][y][1] == 0 or visit[x+1][y][1] > ans:
                    visit[x+1][y][1] = ans
                    Q.append([x,y,0,ans])
                if visit[xx+1][yy][1] == 0 or visit[xx+1][yy][1] > ans:
                    visit[xx+1][yy][1] = ans
                    Q.append([xx,yy,0,ans])
            # 위체크
            if 0<=x-1 and 0<=xx-1 and board[x-1][y] == 0 and board[xx-1][yy] == 0:
                if (x-1==N-1 and y==N-1) or (xx-1==N-1 and yy==N-1):
                    return ans
                if visit[x-1][y][1] == 0 or visit[x-1][y][1] > ans:
                    visit[x-1][y][1] = ans
                    Q.append([x,y,3,ans])
                if visit[xx-1][yy][1] == 0 or visit[xx-1][yy][1] > ans:
                    visit[xx-1][yy][1] = ans
                    Q.append([xx,yy,3,ans])
        if d ==0 or d == 3:
            # 오른쪽체크
            if y+1<N and yy+1<N and board[x][y+1] == 0 and board[xx][yy+1] == 0:
                if (x==N-1 and y+1==N-1) or (xx==N-1 and yy+1==N-1):
                    return ans
                if visit[x][y+1][0] == 0 or visit[x][y+1][0] > ans:
                    visit[x][y+1][0] = ans
                    Q.append([x,y,1,ans])
                if visit[xx][yy+1][0] == 0 or visit[xx][yy+1][0] > ans:
                    visit[xx][yy+1][0] = ans
                    Q.append([xx,yy,1,ans])
            # 왼쪽체크
            if 0<=y-1 and 0<=yy-1 and board[x][y-1] == 0 and board[xx][yy-1] == 0:
                if (x==N-1 and y-1==N-1) or (xx==N-1 and yy-1==N-1):
                    return ans
                if visit[x][y-1][0] == 0 or visit[x][y-1][0] > ans:
                    visit[x][y-1][0] = ans
                    Q.append([x,y,2,ans])
                if visit[xx][yy-1][0] == 0 or visit[xx][yy-1][0] > ans:
                    visit[xx][yy-1][0] = ans
                    Q.append([xx,yy,2,ans])
        
    return answer

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))