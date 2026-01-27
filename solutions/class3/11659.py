import sys

N, M=map(int, sys.stdin.readline().split())

num_list=[0]+list(map(int, sys.stdin.readline().split()))

result_list=[0]*(N+1)
result_list[0]=num_list[0]
for i in range(1, N+1):
    result_list[i]=result_list[i-1]+num_list[i]





for j in range(M):
    start, end=map(int, sys.stdin.readline().split())
    sum=result_list[end]-result_list[start-1]
    print(sum)