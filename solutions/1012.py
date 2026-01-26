from collections import deque
import sys

T=int(sys.stdin.readline())
result=0

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(x,y,M,N,warm):
    q=deque([(x,y)])
    warm[x][y]=0
    while q:
        cur_x, cur_y=q.popleft()
        for way in range(4):
            nx=cur_x+dx[way]
            ny=cur_y+dy[way]
            if 0 <= nx < M and 0 <= ny < N:
                if warm[ny][nx]==1:
                    q.append((nx,ny))
                    warm[ny][nx]=0


for i in range(T):
    M,N,K=map(int, sys.stdin.readline().split())
    warm=[[0]*M for _ in range(N)]
    result=0

    for j in range(K):
        row, col=map(int, sys.stdin.readline().split())
        warm[col][row]=1
    
    for r in range(M):
        for c in range(N):
            if warm[c][r]==1:
                bfs(r,c,M,N,warm)
                result+=1
    
    print(result)

