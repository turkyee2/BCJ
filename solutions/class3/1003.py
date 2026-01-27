def fibonacci(n, fib_table):
    if(fib_table[n]==None):
        if fib_table[n-1]==None:
            fibonacci(n-1, fib_table)
            fib_table[n]=fibo(fib_table[n-1].num0+fib_table[n-2].num0,fib_table[n-1].num1+fib_table[n-2].num1)
        else:
            fib_table[n]=fibo(fib_table[n-1].num0+fib_table[n-2].num0,fib_table[n-1].num1+fib_table[n-2].num1)
    else:
        return
    
class fibo:
    def __init__(self, num0, num1):
        self.num0=num0
        self.num1=num1

fib_table=[None]*41
fib_table[0]=fibo(1,0)
fib_table[1]=fibo(0,1)

T=int(input())
i=0
for i in range(T):
    N=int(input())
    fibonacci(N,fib_table)
    print(fib_table[N].num0, fib_table[N].num1)
    