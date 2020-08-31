def solution(m, musicinfos):
    scale_map = {
        'A': 'A', 'A#': 'a', 'B': 'B',
        'C': 'C', 'C#': 'c', 'D': 'D',
        'D#': 'd', 'E': 'E', 'F': 'F',
        'F#': 'f', 'G': 'G', 'G#': 'g',
        'E#': 'e'
    }

    def convert_melody(m):
        new_m = ''
        N = len(m)
        for i, scale in enumerate(m):
            if scale == '#':
                continue
            elif i + 1 < N and m[i+1] == '#':
                new_m += scale_map[f'{scale}#']
            else:
                new_m += scale
        return new_m

    def convert_hour_to_minutes(time_str):
        h, m = list(map(int, time_str.split(':')))
        return h * 60 + m

    def get_full_melody(start, end, m):
        m_len = len(m)
        duration = end - start
        if duration <= m_len:
            return m[:duration]
        else:
            r = duration // m_len
            d = duration % m_len
            return m * r + m[:d]

    m = convert_melody(m)

    answer = [-1, '(None)']

    for musicinfo in musicinfos:
        start, end, title, melody = musicinfo.split(',')
        start = convert_hour_to_minutes(start)
        end = convert_hour_to_minutes(end)
        melody = convert_melody(melody)
        full_m = get_full_melody(start, end, melody)

        if m in full_m:
            duration = end - start
            if answer[0] < duration:
                answer = [duration, title]

    return answer[1]

m = 'AA'
musicinfos = ['12:00,12:14,HELLO,AAAAAAAAAAAAA', '13:00,13:14,WORLD,AAAAAAAAAA']
print(solution(m, musicinfos))