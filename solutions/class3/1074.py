import sys
N,c,r=map(int, sys.stdin.readline().split())

def find_Z(N,c,r,temp):
    if N==0:
        print(temp)
        return
    n=2**N

    if r<(n/2):
        if c<(n/2):
            find_Z(N-1,r,c,temp)
        else:
            temp=temp+4**(N-1)
            find_Z(N-1,r,c-(n/2),temp)
    else:
        if c<(n/2):
            temp=temp+2*4**(N-1)
            find_Z(N-1,r-(n/2),c,temp)
        else:
            temp=temp+3*4**(N-1)
            find_Z(N-1,r-(n/2),c-(n/2),temp)




find_Z(N,r,c,0)

