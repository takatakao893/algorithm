from collections import deque
n,q=map(int,input().split())
total=0
queue=deque([])
d={}
for _ in range(n):
    name,time=map(str,input().split())
    d[name]=int(time)
    queue.append(name)

while len(queue):
    x=queue.popleft()
    if d[x] > q:
        d[x]-=q
        total+=q
        queue.append(x)
    else:
        total+=d[x]
        print(x,total)