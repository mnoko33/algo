def solution(s):
    def is_palindrome(left, right):
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    N = len(s)
    for i in range(N, 0, -1):
        for j in range(N - i + 1):
            if is_palindrome(j, j + i - 1):
                return i
    return 0
    


print(solution('abcdcba'))
print(solution('abacde'))