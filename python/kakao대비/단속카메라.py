def solution(routes):
    answer = 1
    routes.sort(key=lambda x: -x[1])
    limit = routes[-1][1]
    while routes:
        route = routes.pop()
        if route[0] <= limit:
            continue
        limit = route[1]
        answer += 1
    return answer
