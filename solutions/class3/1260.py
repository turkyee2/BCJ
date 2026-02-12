from collections import deque
import sys

N,M,V=map(int, sys.stdin.readline().split())

edge=[[] for _ in range(N+1)]

for i in range(M):
    a,b=map(int, sys.stdin.readline().split())
    edge[a].append(b)
    edge[b].append(a)

for i in range(1, N + 1):
    edge[i].sort()

DFS=deque()
BFS=deque()

dfs_result=[0]*(N+1)
bfs_result=[0]*(N+1)

DFS.append(V)
BFS.append(V)

while DFS:
    cur=DFS.pop()
    if dfs_result[cur]==0:
        print(cur,end=' ')
        dfs_result[cur]=1
        
        for edges in reversed(edge[cur]):
            if dfs_result[edges]==0:
                DFS.append(edges)
print()

while BFS:
    cur=BFS.popleft()
    if bfs_result[cur]==0:
        print(cur, end=' ')
        bfs_result[cur]=1

        for edges in edge[cur]:
            if bfs_result[edges]==0:
                BFS.append(edges)