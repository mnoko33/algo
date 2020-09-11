def solution(genres, plays):
    genre_dict = dict()
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre in genre_dict:
            genre_dict[genre]['play'] += play
            top2 = genre_dict[genre]['top2']
            top2.append([i, play])
            top2.sort(key=lambda x: (-x[1], x[0]))
            genre_dict[genre]['top2'] = top2[:2]
        else:
            genre_dict[genre] = {
                'play': play,
                'top2': [[i, play]]
            }

    result = list(genre_dict.values())
    result.sort(key=lambda x: -x['play'])
    answer = []
    for genre_info in result:
        answer += [top[0] for top in genre_info['top2']]
    return answer


genres = ["classic", "pop", "classic", "classic"]
plays = [500, 600, 150, 800]
print(solution(genres, plays))