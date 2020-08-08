def solution(name):
    global answer
    answer = 0
    target = 0
    N = len(name)
    right = 0
    left = 0
    name = [x for x in name]
    for idx, _name in enumerate(name):
        if _name != 'A':
            target += 1
            if idx < N // 2:
                right += 1
            else:
                left += 1
    d = -1 if left >= right else 1
    def makeA(i, alpha):
        global answer
        asc = ord(alpha)
        if asc == 65:
            return
        if asc - 65 <= 13:
            name[i] = 'A'
            answer += asc - 65
            return
        else:
            name[i] = 'A'
            answer += 91 - asc
            return
    
    i = 0
    while target > 0:
        if name[i] != 'A':
            makeA(i, name[i])
            target -= 1
            
        if d == 1:
            i = i+1 if i != N-1 else 0
        else:
            i = i-1 if i != 0 else N-1
        if target > 0:
            answer += 1
    return answer


    # test11 failed