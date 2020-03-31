# 메시지 처리 시간
from collections import deque
from heapq import heappush, heappop

M,C = map(int, input().split())
costs = deque()
msg_Q = []
for _ in range(M):
    costs.append(int(input()))
time = 0
while costs:
    msg = costs.popleft()
    # all consumers is running
    if len(msg_Q) == C:
        min_msg = heappop(msg_Q)
        time += min_msg
        # msg_Q안에 모두 처리한 것이 있으면 삭제
        if len(msg_Q) > 0:
            while msg_Q[0] <= min_msg:
                heappop(msg_Q)
        for idx in range(len(msg_Q)):
            msg_Q[idx] -= min_msg
    # msg_Q에 msg 푸쉬
    heappush(msg_Q, msg)

temp = 0
while msg_Q:
        temp = max(temp, heappop(msg_Q))
print(time + temp)


