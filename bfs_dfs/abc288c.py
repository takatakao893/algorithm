import sys
sys.setrecursionlimit(10**6)
n,m=map(int,input().split())
graph=[[] for _ in range(n)]

for _ in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)

judge=[False]*n
s=0

def dfs(i):
    judge[i]=True
    for w in graph[i]:
        if not judge[w]:
            dfs(w)

for i in range(n):
    if not judge[i]:
        s+=1
        dfs(i)

print(m-n+s)
        
