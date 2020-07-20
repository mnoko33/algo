r,c,k = list(map(int, input().split(' ')))
arr = [list(map(int, input().split(' '))) for _ in range(3)]

def R(arr):
    n, m = len(arr), len(arr[0])
    max_cnt = 0
    for i in range(n):
        num_and_cnt = {}
        for j in range(m):
            if arr[i][j] == 0:
                continue
            if arr[i][j] in num_and_cnt.keys():
                num_and_cnt[arr[i][j]] += 1
            else:
                num_and_cnt[arr[i][j]] = 1
        _arr = [[key, num_and_cnt[key]] for key in num_and_cnt.keys()]
        _arr.sort(key=lambda  x: (x[1], x[0]))
        tmp = []
        for k,v in _arr:
            tmp += [k,v]
        tmp = tmp if len(tmp) <= 100 else tmp[:101]
        arr[i] = tmp
        max_cnt = max(max_cnt, len(tmp))
    for i in range(n):
        arr[i] += [0] * (max_cnt - len(arr[i]))
    return arr

def C(arr):
    n, m = len(arr), len(arr[0])
    max_cnt = 0
    tmp = []
    for j in range(m):
        num_and_cnt = {}
        for i in range(n):
            if arr[i][j] == 0:
                continue
            if arr[i][j] in num_and_cnt.keys():
                num_and_cnt[arr[i][j]] += 1
            else:
                num_and_cnt[arr[i][j]] = 1
        _arr = [[key, num_and_cnt[key]] for key in num_and_cnt.keys()]
        _arr.sort(key=lambda  x: (x[1], x[0]))
        
        _tmp = []
        for k,v in _arr:
            _tmp += [k,v]
        _tmp = _tmp if len(_tmp) <= 100 else _tmp[:101]
        max_cnt = max(max_cnt, len(_tmp))
        tmp.append(_tmp)
    arr = [[] for _ in range(max_cnt)]
    for _tmp in tmp:
        for idx in range(max_cnt):
            if idx >= len(_tmp):
                arr[idx].append(0)
            else:
                arr[idx].append(_tmp[idx])
    return arr

answer = 0
while True:
    if len(arr) >= r and len(arr[0]) >= c and arr[r-1][c-1] == k:
        print(answer)
        break
    if answer >= 100:
        print(-1)
        break
    n, m = len(arr), len(arr[0])
    if n >= m:
        arr = R(arr)
    else:
        arr = C(arr)
    answer += 1