from collections import deque
import heapq

def solution(jobs):
    N = len(jobs)
    now = 0
    answer = 0
    jobs.sort(key=lambda x: x[0])
    jobs = deque(jobs)
    waiting_queue = []

    def insert_waiting_queue():
        while True:
            if jobs and jobs[0][0] <= now:
                req_time, running_time = jobs.popleft()
                heapq.heappush(waiting_queue, [running_time, req_time])
            else:
                break

    def do_job():
        return heapq.heappop(waiting_queue)

    while jobs or waiting_queue:
        if jobs:
            insert_waiting_queue()
        if not waiting_queue:
            now = jobs[0][0]
            continue
        running_time, req_time = do_job()
        now += running_time
        answer += now - req_time

    return answer // N


jobs = 	[[0, 3], [1, 9], [2, 6]]
print(solution(jobs))