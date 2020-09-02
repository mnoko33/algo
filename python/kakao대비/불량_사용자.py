from collections import deque

def solution(user_id, banned_id):
    def is_mapping(bid, uid):
        if len(bid) != len(uid):
            return False

        for i in range(len(bid)):
            if bid[i] == '*':
                continue
            if bid[i] != uid[i]:
                return False
        return True

    banned = [[] for _ in range(len(banned_id))]
    for idx, bid in enumerate(banned_id):
        for uid in user_id:
            if is_mapping(bid, uid):
                banned[idx].append(uid)

    result = []
    Q = deque([[0, []]])
    while Q:
        idx, arr = Q.popleft()
        if idx == len(banned):
            arr.sort()
            if not arr in result:
                result.append(arr)
            continue

        for id in banned[idx]:
            if id not in arr:
                Q.append([idx+1, arr+[id]])
    
    return len(result)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]

print(solution(user_id, banned_id))


