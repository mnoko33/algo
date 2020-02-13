def solution(msg):
    answer = []
    D = ['A',"B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    def find_idx(w):
        for i,v in enumerate(D):
            if v == w:
                return i+1
    
    def find_w(idx, msg):
        w = msg[idx]
        while idx < len(msg)-1:
            if w + msg[idx+1] in D:
                w += msg[idx+1]
                idx += 1
            else:
                D.append(w+msg[idx+1])
                break
        return [w, idx]
    
    idx = 0
    while idx < len(msg):
        w, idx = find_w(idx, msg)
        answer.append(find_idx(w))
        idx += 1

    return answer