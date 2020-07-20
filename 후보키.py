def solution(relation):
    global answer
    answer = 0
    n = len(relation[0])
    selected = [1] * n
    
    def unique_check(selected):
        if [0] * len(selected) == selected:
            return False
        target = []
        for rel in relation:
            tmp = []
            for i in range(len(selected)):
                if selected[i] == 1:
                    tmp.append(rel[i])
            if tmp in target:
                return False
            else:
                target.append(tmp)
        return True
    
    def min_check(selected):
        for i in range(len(selected)):
            if selected[i] == 1:
                selected[i] = 0
                if unique_check(selected):
                    selected[i] = 1
                    return False
                selected[i] = 1
        return True
    
    def comb(cnt, idx):
        global answer
        if cnt == idx:
            if unique_check(selected) and min_check(selected):
                answer += 1
            return
    
        selected[idx] = 0
        comb(cnt, idx+1)
        selected[idx] = 1
        comb(cnt, idx+1)
    comb(n, 0)
    
    return answer