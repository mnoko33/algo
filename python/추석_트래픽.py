def solution(lines):
    answer = 1
    N = len(lines)
    new_lines = []
    for line in lines:
        line = line.split(' ')
        e = int(line[1].split(':')[0]) * 3600 + int(line[1].split(':')[1]) * 60 + float(line[1].split(':')[2])
        s = e - float(line[2][:-1])
        s = int(s * 1000 + 1) / 1000
        new_lines.append([s,e])

    for i in range(0, N-1):
        cnt = 1
        s, e = new_lines[i]
        for j in range(i+1, N):
            if new_lines[j][0] < e+1:
                s = new_lines[j][0]
                cnt += 1
        answer = max(answer, cnt)
    return answer