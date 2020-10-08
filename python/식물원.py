def solution(flowers):
    def set_flower(flower):
        start, end = flower
        for i in range(start, end):
            year[i] += 1

    def count_at_least_flowering():
        count = 0
        for day in year:
            if day >= 1:
                count += 1
        return count
    
    year = [0] * 366
    for flower in flowers:
        set_flower(flower)

    return count_at_least_flowering()

print(solution([[2, 5], [3, 7], [10, 11]]))
print(solution([[3, 4],[4, 5], [6, 7], [8, 10]]))