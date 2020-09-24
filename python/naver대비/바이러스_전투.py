from collections import deque

def solution(N, M, Map):
    Map = [[x for x in row] for row in Map]
    for x in Map:
        print(x)
    DR = [0, 1, 0, -1]
    DC = [1, 0, -1, 0]

    def get_virus_dict(r,c):
        virus_dict = {}
        virus = Map[r][c]
        virus_dict[virus] = 1
        Map[r][c] = '*'
        Q = deque([[r, c]])
        while Q:
            r, c = Q.popleft()
            for d in range(4):
                nr = r + DR[d]
                nc = c + DC[d]
                if nr < 0 or nc < 0 or nr >= N or nc >= M:
                    continue
                if Map[nr][nc] == '*':
                    continue
                if Map[nr][nc] == '-':
                    Map[nr][nc] = '*'
                    Q.append([nr, nc])
                    continue
                virus = Map[nr][nc]
                Map[nr][nc] = '*'
                virus_dict[virus] = 1 if virus not in virus_dict else virus_dict[virus] + 1
                Q.append([nr, nc])

        return virus_dict
    
    virus_dict_list = []
    for i in range(N):
        for j in range(M):
            if Map[i][j].isalpha():
                virus_dict = get_virus_dict(i, j)
                virus_dict_list.append(virus_dict)

    def get_virus_war_result(virus_dict):
        virus_kind = list(virus_dict.keys())
        virus_kind.sort(key=lambda k: (-virus_dict[k], k))
        virus = virus_kind[0]
        return [virus, virus_dict[virus]]
    print(virus_dict_list)
    result_dict = {}
    for virus_dict in virus_dict_list:
        virus, cnt = get_virus_war_result(virus_dict)
        result_dict[virus] = cnt if virus not in result_dict else result_dict[virus] + cnt
    result = sorted(result_dict.items(), key=lambda x: x[0])

    answer = ''
    for virus, cnt in result:
        answer += virus + str(cnt)

    return answer

print(solution(5, 7, ['--*AB**', 'AB*A*BA', 'B*-A*BB', '*-A*A**', 'BC*BC*C']))
print(solution(9, 6, ['*****z', '******', 'hh-i*a', '**ih*b', 'c*-***', 'c**---', 'cazbba', 'zz****', '***f**']))