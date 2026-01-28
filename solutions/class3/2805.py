import sys

N,M=map(int, sys.stdin.readline().split())
Trees=[0]*N
Trees=list(map(int, sys.stdin.readline().split()))

max=0

for i in range(N):
    if Trees[i]>max:
        max=Trees[i]
#cur_max=max

low=0
high=max

while high>low:
    mid=(low+high)//2

    sum=int(0)
    for j in range(N):
        if Trees[j]>mid:
            sum+=(Trees[j]-mid)

    if sum>=M:
        result=mid
        low=mid+1
    else:
        high=mid-1

print(result)
"""

temp=M
while temp>0:
    for j in range(N):
        if Trees[j]==cur_max:
            Trees[j]-=1
            temp-=1
    cur_max-=1

print(cur_max)
"""