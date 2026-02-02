from collections import deque
import sys

N,K=map(int, sys.stdin.readline().split())


temp=int(N)
visited=[0]*100001
q=deque()
q.append([temp,0])
while temp!=K:
    temp, t=q.popleft()
    if temp==K:
        print(t)
    for var in (temp-1,temp+1,temp*2):
        if visited[var]!=1 and 0<=var<=100000:
            visited[var]=1
            q.append([var,t+1])

