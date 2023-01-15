# fibonacci
memo=[0]*51
memo[0]=0
memo[1]=1
def init():
    for i in range(2,51):
        memo[i]=memo[i-1]+memo[i-2]

def solve(x):
    init()
    return memo[x]

a={}
def fib(n,a={}):
    if n<=2:
        return 1
    elif n in a:
        return a[n]
    else:
        a[n]=fib(n-1,a)+fib(n-2,a)
        return a[n]

X=int(input())
print(solve(X))
print(fib(50,a))
