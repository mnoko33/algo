from collections import deque

def solution(priorities, location):
    priorities = deque(priorities)
    idxs = deque(list(range(len(priorities))))
    global printed_cnt
    printed_cnt = 0
    def get_first():
        return [priorities.popleft(), idxs.popleft()]

    def is_top_priority(J):
        if not priorities:
            return True
        return J >= max(priorities)

    def print_J():
        global printed_cnt
        printed_cnt += 1

    def redo_priority(J, idx):
        priorities.append(J)
        idxs.append(idx)

    while True:
        J, idx = get_first()
        if is_top_priority(J):
            print_J()
            if idx == location:
                return printed_cnt
        else:
            redo_priority(J, idx)


priorities = [1, 2, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))