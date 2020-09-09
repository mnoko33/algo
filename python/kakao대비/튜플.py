def solution(s):
    arr = sorted([list(map(int, x.split(','))) for x in s[2:-2].split('},{')], key=lambda x: len(x))
    result = []
    for subset in arr:
        for num in subset:
            if num not in result:
                result.append(num)
                break
    return result

print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))