from collections import deque
from bisect import bisect_left
import sys

N=int(input())
X=[]*N
X=list(map(int, sys.stdin.readline().split()))
Y=list(set(X))
Y.sort()

for i in X:
    print(bisect_left(Y,i),end=" ")

