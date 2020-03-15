import heapq

def myGPS(N,M,S,D,U,V,P):
    N,M = map(int, input().split(' '))
    S,D = map(int, input().split(' '))
    Info = []
    for _ in range(M):
        info.append(list(map(int, input().split(' '))))
    # priority Queue
    pq = heapq()
    # distance
    D = [[1000, 1000] for _ in range(N)]



    first_visited = [0] * N
    second_visited = [0] * N
    for (u,v,p) in Info:
        distance = first_visited[u] + p
        if distance < first_visited[v]:
            second_visited[v] = first_visited[v]
            first_visited[v] = distance
            continue
        
        if distance < second_visited[v]:
            second_visited[v] = distance
    
            

    return
