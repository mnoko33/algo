def solution(key, lock):
    def rotate_key(key):
        M = len(key)
        new_key = [[0] * M for _ in range(M)]
        for i in range(M):
            for j in range(M):
                new_key[j][M-1-i] = key[i][j]
        return new_key
    keys = [[], [], [], []]
    
    for key_idx in range(4):
        for i in range(len(key)):
            for j in range(len(key)):
                if key[i][j] == 1:
                    keys[key_idx].append([i, j])
        if key_idx == 3:
            break
        key = rotate_key(key)
    M = len(key)
    N = len(lock)
    # count zero in lock
    cnt = 0 
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                cnt += 1
    # expand lock size
    # N => N + 2(M - 1)
    N += 2 * (len(key) - 1)
    expanded_lock = [[-1] * N for _ in range(N)]
    for i in range(len(lock)):
        for j in range(len(lock)):
            expanded_lock[i + len(key) - 1][j + len(key) - 1] = lock[i][j]

    # check key is possible
    for key in keys:
        for i in range(N-M+1):
            for j in range(N-M+1):
                tmp_cnt = cnt
                for _key in key:
                    nx, ny = i + _key[0], j + _key[1]
                    if expanded_lock[nx][ny] == 1:
                        break
                    if expanded_lock[nx][ny] == 0:   
                        tmp_cnt -= 1
                if tmp_cnt == 0:
                    return True
    return False