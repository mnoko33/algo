def solution(msg):
    import string
    # 사전 초기화
    D = [0] + [x for x in string.ascii_uppercase]
    D_map = {}
    for i,d in enumerate(D):
        if i == 0:
            continue
        D_map[d] = i
    
    def find_idx(alpha):
        return D_map[alpha] if alpha in D_map.keys() else 0
    
    def insert_dict(alpha):
        D_map[alpha] = len(D)
        D.append(alpha)
    
    answer = []
    idx = 0
    while idx < len(msg):
        i = idx
        alpha = msg[idx]
        string = alpha
        idx_num = find_idx(string)
        while True:
            if i >= len(msg) - 1:
                break
            if find_idx(string + msg[i+1]):
                i+=1
                string += msg[i]
                idx_num = find_idx(string)
            else:
                insert_dict(string + msg[i+1])
                break
        answer.append(idx_num)
        idx = i + 1

    return answer


msg = 'KAKAO'
print(solution(msg))