import math

def solution(N, M, map):
    def get_distance(p1, p2):
        v = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        return round(v, 2)
    
    points = []

    for i in range(N):
        for j in range(M):
            if map[i][j] == 1:
                points.append([i, j])
    
    K = len(points)
    answer = -1
    for i in range(K):
        for j in range(i+1, K):
            temp = get_distance(points[i], points[j])
            answer = temp if answer == -1 else min(answer, temp)
    
    return answer if answer > 0 else 0.0

print(solution(3, 4, [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]))
print(solution(3, 4, [[1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]))