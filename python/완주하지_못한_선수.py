def solution(participant, completion):
    hash_list = {}
    for _participant in participant:
        if _participant in hash_list:
            hash_list[_participant] += 1
        else:
            hash_list[_participant] = 1

    for _completion in completion:
        if hash_list[_completion] >= 2:
            hash_list[_completion] -= 1
        else:
            del hash_list[_completion]

    for name in hash_list:
        answer = name
        break
    return answer