def solution(routes):
    answer = []
    routes.sort()
    for route in routes:
        if not answer:
            answer.append(route)
            continue
        s,e = route
        _s, _e = answer[-1]
        if (_s <= s and s <= _e) or (_s <= e and e <= _e):
            answer.pop(-1)
            answer.append([max(s, _s), min(e, _e)])
        else:
            answer.append(route)
    return len(answer)