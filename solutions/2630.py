import sys

N=int(sys.stdin.readline())
matrix=[[0]*N for _ in range(N)]


for i in range(N):
    row=[0]*N
    row=list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        matrix[i][j]=row[j]

white=int(0)
blue=int(0)

def decom(xs,ys,xe,ye):
    global white, blue
    temp_color=matrix[xs][ys]

    exit_flag = False

    for i in range(xs,xe):
        if exit_flag==True:
            break
        for j in range(ys,ye):
            if matrix[i][j]!=temp_color:
                exit_flag=True
                break
            else:
                continue
    if exit_flag==True:
        if int(xs)==int(xe):
            if temp_color==1:
                blue+=1
            else:
                white+=1
            return

        else:
            mid_x=(xs+xe)//2
            mid_y=(ys+ye)//2
            decom(xs,ys,mid_x,mid_y)
            decom(xs,mid_y,mid_x,ye)
            decom(mid_x,ys,xe,mid_y)
            decom(mid_x,mid_y,xe,ye)
    else:
        if temp_color==1:
            blue+=1
        else:
            white+=1
        return


decom(0,0,N,N)
print(white)
print(blue)