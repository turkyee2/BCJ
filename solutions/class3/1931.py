from collections import deque
import sys

N=int(input())
meet = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
meet.sort(key=lambda x: (x[1], x[0]))

temp=0
num=0

for i in range(N):
    if meet[i][0]>=temp:
        temp=meet[i][1]
        num+=1
        
print(num)

