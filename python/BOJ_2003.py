# 수들의 합2

def solution(N, M, nums):
    count = 0
    acc = 0
    p1 = -1
    p2 = -1
    moved_pointer = 0

    def is_end_condition():
        return p1 >= N or p2 >= N

    def move_pointer(p1, p2, moved_pointer):
        if acc < M:
            p2 += 1
            moved_pointer = 2
        else:
            p1 += 1
            moved_pointer = 1

        return [p1, p2, moved_pointer]

    def update_acc(acc, moved_pointer):
        if moved_pointer == 1:
            return acc - nums[p1]
        else:
            return acc + nums[p2]

    def update_count(count, acc):
        if acc == M:
            return count + 1
        return count

    while True:
        p1, p2, moved_pointer = move_pointer(p1, p2, move_pointer)
        if is_end_condition():
            break
        acc = update_acc(acc, moved_pointer)
        count = update_count(count, acc)
    return count

N, M = map(int, input().split())
nums = list(map(int, input().split()))
print(solution(N, M, nums))