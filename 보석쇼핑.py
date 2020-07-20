def solution(gems):
    N = len(gems)
    kinds = list(set(gems))
    gem_dict = {}
    for gem in kinds:
        gem_dict[gem] = 0
    
    left = 0
    right = 0
    gem = gems[left]
    gem_dict[gem] += 1

    answer = [0, N - 1]
    best_length = N
    while left < N - 1 and right < N - 1:
        print('------------------------')
        # 보석을 최소 하나씩 포함하도록 right++
        while right < N - 1:
            right += 1
            gem_dict[gems[right]] += 1
            # 모든 보석을 최소 한 개씩 포함한 경우
            if 0 not in gem_dict.values(): 
                new_length = right - left + 1
                if new_length < best_length:
                    best_length = new_length
                    answer = [left, right]
                break
        print(left, right)
        if 0 in gem_dict.values(): break

        # 모든 보석을 포함하지 않는 케이스가 나올 때까지 left++
        while left < N - 1:
            left += 1
            if gem_dict[gems[left]] == 1 and 0 not in gem_dict.values():
                gem_dict[gems[left]] -= 1
            
            elif gem_dict[gem[left]] == 1 and 0 in gem_dict.values():
                break
        
            
            
            gem_dict[gems[left]] -= 1
            # 모든 보석을 포함하지 않는 케이스가 나온 경우
            if gem_dict[gems[left]] == 0:
                new_length = right - left + 1
                if new_length < best_length:
                    best_length = new_length
                    answer = [left, right]
                break

        print(left, right)




    return [answer[0] + 1, answer[1] + 1] 


# print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
# print(solution(["XYZ", "XYZ", "XYZ"]))
# print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))