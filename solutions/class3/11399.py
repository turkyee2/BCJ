N=int(input())
P_list=list(map(int,input().split()))

P_list.sort()
time=0
for i in range(0,N):
    time=time+(P_list[i]*(N-i))

print(time)

