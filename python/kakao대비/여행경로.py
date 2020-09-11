def solution(tickets):
    flight_info = dict()
    for dep, des in tickets:
        if dep in flight_info:
            flight_info[dep].append(des)
        else:
            flight_info[dep] = [des]
    
    answer = []
    path = ['ICN']
    def depart_from_city(dep):
        if not tickets:
            answer.append([city for city in path])
            return
        if dep not in flight_info:
            return
        for des in flight_info[dep]:
            if [dep, des] not in tickets:
                continue
            tickets.remove([dep, des])
            path.append(des)
            depart_from_city(des)
            tickets.append([dep, des])
            path.pop()

    depart_from_city('ICN')
    return sorted(answer)[0]

tickets = [['ICN','A'],['ICN','A'],['A','ICN'],['A','B']]
print(solution(tickets))