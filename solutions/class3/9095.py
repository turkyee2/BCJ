import sys

N=int(input())

comb_num=[0]*15
comb_num[1]=1
comb_num[2]=1
comb_num[3]=1
count_max=int(1)


def count_comb(num):
    global count_max
    if int(num)<=int(count_max):
        return
    else:
        for j in range(count_max+1,(num+1)):
            comb_num[j]+=comb_num[j-1]
            comb_num[j+1]+=comb_num[j-1]
            comb_num[j+2]+=comb_num[j-1]
        count_max=num
        


for i in range(N):
    num=int(sys.stdin.readline())
    count_comb(num)
    print(comb_num[num])