def solution(clothes):
    clothes_list = {}
    for [name, kind] in clothes:
        if kind in clothes_list:
            clothes_list[kind] += 1
        else:
            clothes_list[kind] = 1

    answer = 1
    for cnt in clothes_list.values():
        answer *= cnt + 1

    return answer - 1