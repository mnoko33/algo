def solution(clothes):
    cloth_dict = {}
    for _, cloth_category in clothes:
        if cloth_category in cloth_dict:
            cloth_dict[cloth_category] += 1
        else:
            cloth_dict[cloth_category] = 1
            
    answer = 1
    for case in cloth_dict.values():
        answer *= case + 1
    return answer - 1

print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))