from collections import deque

def check_condition(password):
    VOWEL = ['a', 'e', 'i', 'o', 'u']
    vowel_cnt = 0
    consonant_cnt = 0
    for char in password:
        if char in VOWEL:
            vowel_cnt += 1
        else:
            consonant_cnt += 1
    return vowel_cnt >= 1 and consonant_cnt >= 2

def make_password_set(L, char_list):
    answer = []
    init = ('', 0)
    Q = deque()
    Q.append(init)
    while Q:
        password_set, idx = Q.popleft()
        if len(password_set) >= L:
            if check_condition(password_set):
                answer.append(password_set)
            continue
        if idx >= len(char_list):
            continue
        Q.append((password_set + char_list[idx], idx + 1))
        Q.append((password_set, idx + 1))
    
    answer.sort()
    for x in answer:
        print(x)
    
L, C = map(int, input().split())
char_list = input().split(' ')
make_password_set(L, sorted(char_list))