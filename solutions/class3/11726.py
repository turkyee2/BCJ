import sys

n=int(input())

fibo=[0]+[1]+[2]+[0]*(n-2)


for i in range(3, n+1):
    fibo[i]=(fibo[i-2]+fibo[i-1])%10007

print(fibo[n])