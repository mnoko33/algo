def solution(histogram):
    def calculate_area(p1, p2):
        height = min(histogram[p1], histogram[p2])
        width = p2 - p1 - 1
        return height * width
    
    answer = 0
    p1 = 0
    p2 = len(histogram)-1
    answer = calculate_area(p1, p2)
    while p1 <= p2:
        increase_p1 = calculate_area(p1+1, p2)
        decrease_p2 = calculate_area(p1, p2-1)
        if increase_p1 > decrease_p2:
            answer = max(answer, increase_p1)
            p1 += 1
        else:
            answer = max(answer, decrease_p2)
            p2 -= 1
    return answer

print(solution([2, 2, 2, 3]))
print(solution([6, 5, 7, 3, 4, 2]))