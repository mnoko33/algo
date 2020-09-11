import heapq

def solution(operations):
    max_Q = []
    min_Q = []
    removed = []
    
    def delete_max():
        v = heapq.heappop(max_Q) * -1
        min_Q.remove(v)

    def delete_min():
        v = heapq.heappop(min_Q)
        max_Q.remove(v * -1)

    def insert(v):
        heapq.heappush(max_Q, -1 * v)
        heapq.heappush(min_Q, v)

    def parse_operation(oper):
        order, value = oper.split(' ')
        return [order, int(value)]

    for operation in operations:
        order, value = parse_operation(operation)
        if order == 'D' and value == -1:
            if min_Q:
                delete_min()
        elif order == 'D' and value == 1:
            if max_Q:
                delete_max()
        else:
            insert(value)

    size = len(min_Q)
    if size == 0:
        return [0, 0]
    if size == 1:
        v = heapq.heappop(min_Q)
        return [max(v, 0), min(v, 0)]
    return [heapq.heappop(max_Q) * -1, heapq.heappop(min_Q)]

operations = ['I 4', 'I 3', 'I 2', 'I 1', 'D 1', 'D 1', 'D -1', 'D -1', 'I 5', 'I 6']
print(solution(operations))