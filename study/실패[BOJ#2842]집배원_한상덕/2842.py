import deque

def deliver(N, map, height):
    Q = deque()
    P = []
    K_list = []
    for i in range(N):
        for j in range(N):
            target = map[i][k]
            if target == 'P':
                P = [i, j]
            if target == 'K':
                K_list.append([i,j])
    
    return



N = 3
Map = [['K','.','P'], ['.','.','.'], ['K','.','K']]
height = [[3,3,4], [9,5,9], [8,3,7]]



