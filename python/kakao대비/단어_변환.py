from collections import deque

def solution(begin, target, words):
    def is_convertable(x, y):
        cnt = 0
        for sub_x, sub_y in zip(x,y):
            if sub_x != sub_y:
                cnt += 1 
            if cnt > 1:
                return False
        return True

    Q = deque([[begin, 0]])
    used_word = []
    while Q:
        begin, cnt = Q.popleft()
        for word in words:
            if is_convertable(begin, word):
                if word == target:
                    return cnt+1
                Q.append([word, cnt+1])
                used_word.append(word)
        words = [word for word in words if word not in used_word]
    return 0