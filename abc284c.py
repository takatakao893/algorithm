from collections import defaultdict,deque
# breadth first search
def bfs(i):
    queue=deque([i])
    while len(queue):
        x=queue.popleft()
        for y in l[x]:
            if not y in s:
                s.add(y)
                bool[y]=True
                queue.append(y)


N,M=map(int,input().split())
l=defaultdict(list)
for _ in range(M):
    u,v=map(int,input().split())
    l[u].append(v)
    l[v].append(u)

bool=[False]*(N+1)
s={1}
cnt=0
for i in range(1,N+1):
    if bool[i]==False:
        bfs(i)
        cnt+=1
print(cnt)
