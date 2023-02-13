N,M=map(int,input().split())
a=list(map(int,input().split()))
l=list(range(1,N+1))
ans=[]
stack=[]
for x in l:
    if not x in a:
        ans.append(x)
        while stack:
            t=stack.pop()
            ans.append(t)
    else:
        stack.append(x)
print(*ans)
