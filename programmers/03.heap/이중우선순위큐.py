def solution(operations):
    answer = []
    for operation in operations:
        order, v = operation.split(' ')
        if order == 'I':
            answer.append(int(v))
        else:
            if v == '1' and answer:
                answer.remove(max(answer))
            elif v == '-1' and answer:
                answer.remove(min(answer))
    if not answer:
        answer.append(0)
    return [max(answer), min(answer)]


# 힙을 사용해서 풀어보자