import sys
from collections import deque

N,M=map(int, sys.stdin.readline().split())

edges=[[] for _ in range(N+1)]
nodes=[1]*(N+1)

for i in range(M):
    a,b=map(int, sys.stdin.readline().split())
    edges[a].append(b)
    edges[b].append(a)
conn=deque()

result=0

for j in range(1,N+1):
    if nodes[j]==1:
        result+=1
        conn.append(j)
        nodes[j]=0

        while conn:
            cur=conn.popleft()
            for k in edges[cur]:
                if nodes[k]==1:
                    nodes[k]=0
                    conn.append(k)

            
print(result)