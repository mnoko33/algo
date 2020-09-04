def solution(gems):
    N = len(gems)
    answer_list = []
    apeach_gems = {}
    gem_cnt = len(list(set(gems)))

    start = 0
    end = 0
    while start < N and end < N:
        # end 
        while end < N:
            gem = gems[end]
            if gem in apeach_gems:
                apeach_gems[gem] += 1
            else:
                apeach_gems[gem] = 1
            end += 1
            # 모두 최소 한 개 씩 가지고 있는 경우
            if len(apeach_gems.keys()) == gem_cnt:
                answer_list.append([start+1, end])
                break
        # 최소 한 개씩 가지지 못한 경우
        if len(apeach_gems.keys()) < gem_cnt:
            break
        # start 
        while start < N:
            gem = gems[start]
            if apeach_gems[gem] > 1:
                apeach_gems[gem] -= 1
            else:
                del apeach_gems[gem]
            start += 1

            if len(apeach_gems.keys()) < gem_cnt:
                break
            answer_list.append([start+1, end])

    answer_list.sort(key=lambda x: (x[1] - x[0], x[0]))
    return answer_list[0]


gems = 	["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))