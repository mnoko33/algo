def solution(dirs):
    order = {
        'D': [1, 0],
        'U': [-1, 0],
        'R': [0, 1],
        'L': [0, -1]
    }
    routes = []
    x, y = 5, 5
    for dir in dirs:
        nx = x + order[dir][0]
        ny = y + order[dir][1]
        if nx < 0 or ny < 0 or nx >= 11 or ny >= 11:
            continue
        if [x,y,nx,ny] not in routes and [nx,ny,x,y] not in routes:
            routes.append([x,y,nx,ny])
        x = nx
        y = ny
        
    return len(routes)

dirs = 'ULURRDLLU'
print(solution(dirs))