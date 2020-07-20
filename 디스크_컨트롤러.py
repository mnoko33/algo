import heapq

def solution(jobs):
    now = 0
    answer = 0
    h = []
    N = len(jobs)
    job_list = []
    heapq.heapify(jobs)
    
    while jobs or job_list:
        if jobs:
            while True:
                if not jobs:
                    break
                if jobs[0][0] > now:
                    break
                
                job = heapq.heappop(jobs)
                job[0], job[1] = job[1], job[0]
                heapq.heappush(job_list, job)
        if not job_list:
            now = jobs[0][0]
            continue
        job = heapq.heappop(job_list)
        answer += now - job[1] + job[0]
        now += job[0]
        
    return answer // N

jobs = [[0, 3], [1, 9], [2, 6]]	
print(solution(jobs))