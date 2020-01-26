def solution(priorities, location):
    answer = 0
    while priorities:    
        priority = priorities.pop(0)
        if not priorities:
            return answer + 1
        if priority >= max(priorities):
            answer += 1
            if location == 0:
                return answer
            else:
                location -= 1
        else:
            priorities.append(priority)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1

    return answer