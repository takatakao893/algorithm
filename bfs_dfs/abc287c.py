from sys import stdin
from collections import deque

def bfs(graph):
    queue=deque([[0,-1]])
    node=[False]*n
    node[0]=True
    judge=True
    while queue:
        u,prev=queue.popleft()
        if len(graph[u])>2: # ノードに2辺より多くつかない
            judge=False
        for w in graph[u]:
            if w==prev: # 前のノードは無視
                continue
            if node[w]:
                judge=False # 一度通ったノードなら
                continue
            node[w]=True
            queue.append([w,u])
    if not all(node):
        judge=False
    return judge

readline=stdin.readline
n,m=map(int,readline().split())
graph=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(lambda x:int(x)-1,readline().split())
    graph[a].append(b)
    graph[b].append(a)

print("Yes" if bfs(graph) else "No")
    