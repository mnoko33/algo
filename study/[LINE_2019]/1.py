# 메시지 처리 시간
from collections import deque

M,C = map(int, input().split())
costs = [int(input()) for _ in range(M)]

class Message_Q:
    def __init__(self, C):
        self.consumers_cnt = C
        self.consumers = [0] * consumers_cnt
        self.max_cnt = 10
        self.time = 0

    def get_message(self, cost):
        flag = False
        for idx in range(self.consumers_cnt):
            # 해당 컨슈머는 더이상 메시지를 처리할 수 없는 상황
            if self.consumers[idx] > 0:
                continue
            else:
                self.consumers[idx] = cost
                flag = True
        
    def refresh_consumers(self):
        temp_min = 0xffff
        for idx in range(self.consumers_cnt):
            temp_min = self.consumers[idx] 
