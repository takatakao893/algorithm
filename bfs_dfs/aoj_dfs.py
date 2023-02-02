import sys
sys.setrecursionlimit(10**8)
readline=sys.stdin.readline
n=int(readline())
ukv=[list(map(int,readline().split())) for _ in range(n)]
d=[0]*(n+1)
f=[0]*(n+1)
now=1
def dfs(x):
    global now
    d[x]=now
    now+=1
    for i in range(ukv[x-1][1]):
        if (d[ukv[x-1][2+i]]!=0):
            continue
        dfs(ukv[x-1][2+i])
    f[x]=now
    now+=1
    return
for i in range(n):
    if (d[i+1]==0):
        dfs(i+1)
for i in range(n):
    print(i+1,d[i+1],f[i+1])
    