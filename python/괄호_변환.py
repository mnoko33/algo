def solution(p):
    def check(s):
        S = []
        for _s in s:
            if _s == '(':
                S.append(_s)
            else:
                if len(S) == 0:
                    return False
                S.pop(-1)
        if len(S) == 0:
            return True
        return False
    
    def seperate(s):
        left, right = 0, 0
        
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left != 0 and right != 0 and left == right:
                break
        return [s[:i+1], s[i+1:]]

    def convert(s):
        tmp = ''
        for x in s[1:-1]:
            if x == ')':
                tmp += '('
            else:
                tmp += ')'
        return tmp

    def main(p):
        if check(p):
            return p

        u, v = seperate(p)
        if check(u):
            return u + main(v)
        return '(' + main(v) + ')' + convert(u)

    return main(p)


print(solution(")("))