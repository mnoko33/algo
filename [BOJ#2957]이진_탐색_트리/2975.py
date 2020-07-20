import sys
sys.stdin = open('2957.txt', 'r')

N = int(input())
C = 0
temp = {}
for _ in range(N):
    i = int(input())
    if len(temp) == 0:
        temp[i] = 0
    else:
        
