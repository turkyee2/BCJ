from collections import deque
import sys

M,N=map(int, sys.stdin.readline().split())
tom=[]
queue=deque()
isPossible=0

for i in range(N):
    row=list(map(int, sys.stdin.readline().split()))
    tom.append(row)
    for j in range(M):
        if row[j]==1:
            queue.append((i,j))

dx=[1,-1,0,0]
dy=[0,0,1,-1]

while queue:
    cur=queue.popleft()
    for k in range(4):
        
        c=cur[0]+dx[k]
        r=cur[1]+dy[k]
        if 0<=c<N and 0<=r<M and tom[c][r]==0:
            tom[c][r]=tom[cur[0]][cur[1]]+1
            queue.append((c,r))
    

date=0

for a in range(N):
    for b in range(M):
        if tom[a][b]==0:
            isPossible=1
            break
        elif tom[a][b]>date:
            date=tom[a][b]

if isPossible==1:
    print(-1)
else:
    print(date-1)