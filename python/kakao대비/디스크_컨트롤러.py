import heapq
from collections import deque

def solution(jobs):
    jobs.sort(key=lambda x: x[0])
    jobs = deque(jobs)
    waiting_queue = []
    result = []
    now = 0
    while jobs or waiting_queue:
        while jobs and jobs[0][0] <= now:
            job = jobs.popleft()
            heapq.heappush(waiting_queue, [job[1], job[0]])
        if not waiting_queue:
            time = jobs[0][0]
            while jobs and jobs[0][0] <= time:
                job = jobs.popleft()
                heapq.heappush(waiting_queue, [job[1], job[0]])
        running_time, request_time = heapq.heappop(waiting_queue)
        if request_time > now:
            now = request_time
        result.append(now - request_time + running_time)
        now += running_time
    return sum(result) // len(result)

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))