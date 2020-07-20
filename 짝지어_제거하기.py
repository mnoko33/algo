def solution(s):
    stack = []
    for x in s:
        if not stack or stack[-1] != x:
            stack.append(x)
        else:
            stack.pop(-1)

    return 1 if not stack else 0

print(solution('baabaa'))
print(solution('cdcd'))