# https://www.acmicpc.net/problem/14719

def solution(H, W, blocks):
    answer = 0
    for i in range(W):
        left = None
        right = None
        # for left height
        for j in range(i):
            if blocks[i] >= blocks[j]:
                continue
            if not left or blocks[left] <= blocks[j]:
                left = j
        if left == None:
            continue
        # for right height
        for k in range(i+1, W):
            if blocks[i] >= blocks[k]:
                continue
            if not right or blocks[right] <= blocks[k]:
                right = k
            if blocks[left] <= blocks[right]:
                break
        if left != None and right != None:
            answer += min(blocks[left], blocks[right]) - blocks[i]
    return answer


H = 4
W = 8
blocks = [3, 0, 1, 4]
print(solution(H, W, blocks))
