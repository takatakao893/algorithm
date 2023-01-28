import bisect
N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
B.sort()
ans=10e10
for a in A:
    x=bisect.bisect_left(B,a)
    if 0<=x-1<M:
        b1=B[x-1]
        ans=min(ans,abs(a-b1))
    if 0<=x<M:
        b2=B[x]
        ans=min(ans,abs(a-b2))
print(ans)