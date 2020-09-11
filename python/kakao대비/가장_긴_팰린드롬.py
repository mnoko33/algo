def solution(s):
    if not s:
        return 0
    answer = 1
    def get_single_palindrome_length(s, i):
        left, right = i, i
        length = 1
        while True:
            left -= 1
            right += 1
            if left < 0 or right >= len(s):
                break
            if s[left] != s[right]:
                break
            length += 2
        return length
    
    def get_double_palindrome_length(s, i):
        left, right = i, i+1
        length = 0
        while True:
            if left < 0 or right >= len(s):
                break
            if s[left] != s[right]:
                break
            length += 2
            left -= 1
            right += 1
        return length

    for i in range(len(s)):
        answer = max(answer, get_single_palindrome_length(s, i), get_double_palindrome_length(s, i))
    
    return answer


s = 'abcdcba'
print(solution(s))