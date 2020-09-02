def solution(n, t, m, timetable):
    def convert_time_to_min(time):
        hh, mm = list(map(int, time.split(':')))
        return hh * 60 + mm

    def convert_min_to_time(time):
        hh = time // 60
        mm = time % 60
        str_hh = str(hh) if hh >= 10 else f'0{hh}'
        str_mm = str(mm) if mm >= 10 else f'0{mm}' 
        return f'{str_hh}:{str_mm}'

    answer = 0
    deadline = 9 * 60
    timetable = [convert_time_to_min(time) for time in sorted(timetable)]
    while n > 0:
        n -= 1
        bus_in = []
        new_timetable = []
        for idx, time in enumerate(timetable):
            if len(bus_in) < m and time <= deadline:
                bus_in.append(time) 
            else:
                new_timetable.append(time)

        timetable = new_timetable
        deadline += t

    if len(bus_in) < m:
        return convert_min_to_time(deadline - t)
    else:
        return convert_min_to_time(bus_in[-1] - 1)


n = 1
t = 1
m = 5
timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]
print(solution(n, t, m, timetable))