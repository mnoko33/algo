def solution(m, musicinfos):
    convert = {
        "C": "M",
        "D": "N",
        "F": "O",
        "G": "P",
        "A": "Q"
    }

    answer = "(None)"
    for i in range(len(m)-2, -1, -1):
        if m[i] in ["C", "D", "F", "G", "A"] and m[i+1] == "#":
            m = m[:i] + convert[m[i]] + m[i+2:]

    for musicInfo in musicinfos:
        [start,end,title,scale] = musicInfo.split(',')
        for i in range(len(scale)-2, -1, -1):
            if scale[i] in ["C", "D", "F", "G", "A"] and scale[i+1] == "#":
                scale = scale[:i] + convert[scale[i]] + scale[i+2:]
        start = int(start.split(':')[0]) * 60 + int(start.split(':')[1])
        end = int(end.split(':')[0]) * 60 + int(end.split(':')[1])
        music_length = len(scale)
        play_length = end-start
        
        if play_length > music_length:
            scale *= play_length // music_length
            scale += scale[:play_length%music_length]
        else:
            scale = scale[:end-start]

        if m in scale:
            if answer == "(None)":
                answer = [play_length, title]
            else:
                if play_length > answer[0]:
                    answer = [play_length, title]
    
    return answer if answer == "(None)" else answer[1]