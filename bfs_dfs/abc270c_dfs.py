from collections import deque
N,X,Y=map(int,input().split())
dict_t={}
ref={}
for i in range(N+1):
    dict_t[i]=[]
    ref[i]=-1

for _ in range(N-1):
    u,v=map(int,input().split())
    dict_t[u].append(v)
    dict_t[v].append(u)

queue=deque([X])
ref[X]=-2

while len(queue):
    x=queue.popleft()
    for i in dict_t[x]:
        if ref[i]==-1:
            ref[i]=x
            queue.append(i)

ans=[]
while Y!=-2:
    ans.append(Y)
    Y=ref[Y]
print(*ans[::-1])