def solution(record):
    answer = []
    tmp_answer = []
    mapping = {}
    for rec in record:
        rec = rec.split(' ')
        if len(rec) == 2:  # leave
            tmp_answer.append([rec[1], rec[0]])
            continue
        if rec[0] == "Change":
            mapping[rec[1]] = rec[2]
            continue
        mapping[rec[1]] = rec[2]
        tmp_answer.append([rec[1], rec[0]])
    for tmp in tmp_answer:
        if tmp[1] == "Enter":
            answer.append(f'{mapping[tmp[0]]}님이 들어왔습니다.')
        else:
            answer.append(f'{mapping[tmp[0]]}님이 나갔습니다.')
    return answer