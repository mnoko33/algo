import sys
sys.stdin = open('2843.txt', 'r')

N = int(input())
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def Q1(self):
        if not self.next:
            print(self.data)
            return
        _next = self.next
        while _next != None:
            # 무한루프
            if _next.data == self.data:
                loop_list.append(self.data)
                print("CIKLUS")
                return
            # 다음 진행
            if _next.next == None:
                print(_next.data)
                return
            _next = _next.next

    def Q2(self):
        self.next = None
        loop_list = []

arr = [Node(i) for i in range(N+1)]
line = list(map(int, input().split(' ')))
for i in range(1, N+1):
    arr[i].next = arr[line[i-1]]
Q = int(input())
loop_list = []
for _ in range(Q):
    question, idx = map(int, input().split(' '))
    if idx in loop_list and question == 1:
        print("CIKLUS")
        continue
    if idx in loop_list and question == 2:
        loop_list = []
    if question == 1:
        arr[idx].Q1()
    else:
        arr[idx].Q2()
