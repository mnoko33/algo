def solution(heights):
    answer = [0 for _ in range(len(heights))]
    for i in range(len(heights)):
        top = heights[i]
        for j in range(i+1, len(heights)):
            if top > heights[j]:
                answer[j] = i + 1
            else:
                break
                
    return answer