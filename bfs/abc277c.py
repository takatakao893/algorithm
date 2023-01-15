from collections import defaultdict,deque
N=int(input())
l=defaultdict(list)
for _ in range(N):
    a,b=map(int,input().split())
    l[a].append(b)
    l[b].append(a)

s={1}
queue=deque([1])
while len(queue):
    x=queue.popleft()
    for y in l[x]:
        if not y in s:
            s.add(y)
            queue.append(y)
print(max(s))
