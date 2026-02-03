from collections import deque
import sys

n,m=map(int, sys.stdin.readline().split())

Map=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]

start=[0,0]
for i in range(n):
    for j in range(m):
        if Map[i][j]==2:
            start=[i,j]
            break

mapQue=deque()
mapQue.append(start)
Map[start[0]][start[1]]=0


def isTrue():
    [N,M]=mapQue.popleft()

    if N+1<n:
         if Map[N+1][M]==1:
            Map[N+1][M]=Map[N][M]+1
            mapQue.append([N+1,M])
    if M+1<m:
         if Map[N][M+1]==1:
            Map[N][M+1]=Map[N][M]+1
            mapQue.append([N,M+1])
             
    if M-1>=0:
        if Map[N][M-1]==1:
            Map[N][M-1]=Map[N][M]+1
            mapQue.append([N,M-1])
    if N-1>=0:
        if Map[N-1][M]==1:
            Map[N-1][M]=Map[N][M]+1
            mapQue.append([N-1,M])


while mapQue:
     isTrue()


for i in range(n):
    print(*Map[i])