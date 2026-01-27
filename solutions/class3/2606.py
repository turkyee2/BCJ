from collections import deque
import sys

queue = deque()

node_num=int(sys.stdin.readline().strip())
matrix=[[0]*(node_num+1) for _ in range(node_num+1)]

result=[0]*(node_num+1)
result[1]=1
queue.append(1)
edge_num=int(input())
for i in range(edge_num):
    com1,com2=map(int, sys.stdin.readline().strip().split())
    matrix[com1][com2]=1
    matrix[com2][com1]=1
    
while queue:
    x=queue.popleft()
    for a in range(node_num):
         if matrix[x][a]==1 and result[a]==0 :
             result[a]=1
             queue.append(a)

vir_num=0
int(vir_num)
for k in range(node_num):
    if(result[k]==1):
         vir_num+=1

print(vir_num)
