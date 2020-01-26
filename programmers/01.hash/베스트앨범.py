def solution(genres, plays):
    answer = []
    sum_dict = {} # 장르의 총 재생 횟수
    list_dict = {} # 장르별 우선순위 2개
    for idx, genre in enumerate(genres):
        if genre in sum_dict:
            sum_dict[genre] += plays[idx]
            top2 = list_dict[genre]
            top2.append((idx, plays[idx]))
            list_dict[genre] = sorted(top2, key=lambda x: x[1], reverse=True)[:2]
        else:
            sum_dict[genre] = plays[idx]
            list_dict[genre] = [(idx, plays[idx])]
    sum_dict = sorted(sum_dict.items(), key=lambda x: x[1], reverse=True)
    for genre in sum_dict:
        top2 = list_dict[genre[0]]
        for x in top2:
            answer.append(x[0])
    return answer