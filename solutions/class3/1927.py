from collections import deque
import sys

N=int(sys.stdin.readline())
heap=[0]*100001
heapMax=1
def insert(val):
    if loc!=0 and heap[loc//2]>val:
        heap[loc]=heap[loc//2]
        heap[loc//2]=val
        loc=loc//2
        insert(val)

def min():
    if heapMax==1:
        print(0)
        return
    print(heap[1])
    heap[1]=heap[heapMax]

    cur = 1
    while (cur * 2) <= heapMax:
        child = cur * 2 
        if child + 1 <= heapMax and heap[child+1] < heap[child]:
            child += 1
            
        if heap[cur] > heap[child]:
            heap[cur], heap[child] = heap[child], heap[cur]
            cur = child
        else:
            break



for i in range(N):
    new=int(sys.stdin.readline())
    if new==0:
        loc=1
        min()
        heapMax-=1
    else:
        heapMax+=1
        loc=heapMax
        heap[loc]=new
        insert(new)