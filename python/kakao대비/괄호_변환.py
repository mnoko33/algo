def solution(p):
    def seperate_to_u_and_v(p):
        cnt1 = 0
        cnt2 = 0
        p = [s for s in p]
        for i, s in enumerate(p):
            if s == '(':
                cnt1 += 1
            else:
                cnt2 += 1
            if cnt1 > 0 and cnt2 > 0 and cnt1 == cnt2:
                break
        return [''.join(p[:i+1]), ''.join(p[i+1:])]

    def check_right(p):
        stack = []
        for s in p:
            if s == '(':
                stack.append(s)
            else:
                if not stack:
                    return False
                stack.pop()
        return len(stack) == 0

    def main(p):
        if p == '':
            return ''

        u, v = seperate_to_u_and_v(p)

        if check_right(u):
            return u + main(v)

        new_str = '(' + main(v) + ')'
        return new_str + ''.join(['(' if s == ')' else ')' for s in [s for s in u][1:-1]])

    return main(p)

