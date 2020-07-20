def solution(n, t, m, timetable):
    def convert(s):
        h,m = list(map(int, s.split(':')))
        return h * 60 + m

    def nth_bus(first, _n, t):
        return first + _n * t
    
    def deconvert(num):
        h = str(num // 60)
        m = str(num % 60)
        if len(h) == 1:
            h = '0'+h
        if len(m) == 1:
            m = '0'+m
        return h+':'+m
    timetable.sort()
    answer = ''
    first = 540
    max_late = nth_bus(first, n-1, t)
    idx = 0 # timetable idx
    # n번차 운행
    for _n in range(n):
        # 마지막 운행이 아닐때
        if _n < n-1:
            # 남은 자리
            limit = m
            # 버스 출발시간
            now = nth_bus(first, _n, t)
            # 더 이상 탈 수 있는 사람이 없을 때 => True
            bus_start = False
            while True:
                # 다음 크루가 탈 수 있을 때
                if now >= convert(timetable[idx]):
                    print(str(idx+1) + '번 째 크루 ' + timetable[idx] + ' 에 탑승')
                    limit -= 1
                # 다음 크루가 탈 수 없기 때문에 버스는 출발한다
                else:
                    bus_start = True
                # 버스가 출발했다면 지금 크루부터 검사해야한다
                if bus_start == True:
                    break
                # 지금 크루가 마지막으로 버스를 탔다면 다음 크루부터 검사해야한다
                if limit == 0:
                    idx += 1
                    break
                # 그런데 지금 크루가 마지막 크루라면?
                if idx == len(timetable) - 1:
                    last_bus = nth_bus(first, n-1, t)
                    return deconvert(last_bus)    
                idx += 1 
        # 마지막 운행일 때
        else:
            # 일단 지금 타려는 크루보다 1분 빨리오면 무조건 탈 수 있다
            max_late = convert(timetable[idx]) - 1
            # 버스 출발시간
            now = nth_bus(first, _n, t)
            # 정원
            limit = m
            while True:
                # 크루가 탈 수 있을 때
                if now >= convert(timetable[idx]):
                    limit -= 1
                    # 일단 이 크루보다 1분 빨리타면 무조건 탈 수는 있다
                    max_late = convert(timetable[idx]) - 1
                # 크루가 탈 수 없다
                else:
                    if limit > 0:
                        return(deconvert(now))
                    else:
                        return(deconvert(convert(timetable[idx-1]) - 1))  
                # 정원이 풀이라면?
                if limit == 0:
                    return deconvert(max_late)
                # 정원초과는 아닌데 지금 크루가 마지막 크루라면?
                if idx == len(timetable) - 1:
                    last_bus = nth_bus(first, n-1, t)
                    return deconvert(last_bus)   
                idx += 1     
    return deconvert(max_late)

print(solution(	1, 1, 1, ["23:59"]))