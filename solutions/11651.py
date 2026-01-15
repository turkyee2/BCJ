N=input()

class nd:
    def __init__(self, x,y):
         self.x=x
         self.y=y

nds=[]

for i in range(int(N)):
    xy=list(map(int, input().split()))
    nds.append(nd(xy[0],xy[1]))
    
nds.sort(key=lambda s: (s.y, s.x))



for j in nds:
    print(j.x, j.y)