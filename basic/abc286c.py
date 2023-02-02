from sys import stdin
N,A,B=map(int,stdin.readline().split())
S=stdin.readline()
res=10e18
for j in range(N):
    tmp=A*j
    for i in range(N//2):
        if S[(i+j)%N]!=S[(N+j-i-1)%N]:
            tmp+=B
    res=min(res,tmp)
print(res)
        