from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
N,X,Y=map(int,input().split())
X-=1
Y-=1
l=defaultdict(list)
for _ in range(N-1):
    u,v=map(int,input().split())
    u-=1
    v-=1
    l[u].append(v)
    l[v].append(u)

def dfs(cur,par):
    if cur==Y:
        print(*ans)
        return
    else:
        for to in l[cur]:
            if to==par:
                continue
            else:
                ans.append(to+1)
                dfs(to,cur)
                ans.pop()

ans=[X+1]
dfs(X,-1)
