from collections import deque
import sys

N,M=map(int, sys.stdin.readline().split())

unheard={}

for i in range(N):
    name=sys.stdin.readline().strip()
    unheard[name]=1

result=[]
for j in range(M):
    unseek=sys.stdin.readline().strip()
    if unseek in unheard:
        result.append(unseek)

result.sort()

print(len(result))
for rst in result:
    print(rst)