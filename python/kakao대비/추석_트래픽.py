def solution(lines):
    # 주어진 Line을 [start_time, closed_time]로 수정하는 함수
    def trim_line(line):
        def convert_time_to_sec(time):
            HOUR2SEC, MIN2SEC = 3600, 60
            hh, mm, ss = list(map(float, time.split(':')))

            return hh * HOUR2SEC + mm * MIN2SEC + ss

        _, time, duration = line.split(' ')

        end = convert_time_to_sec(time)
        duration = float(duration[:-1])
        start = int((end - duration + 0.001)*1000)/1000
        return [start, end]
    
    lines = [trim_line(line) for line in lines]
    answer = 0
    N = len(lines)
    for i in range(N):
        cnt = 1
        limit = lines[i][1] + 1
        for j in range(i+1, N):
            if lines[j][0] < limit:
                cnt += 1
        answer = max(cnt, answer)
    return answer

lines = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
print(solution(lines))