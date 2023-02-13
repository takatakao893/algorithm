from itertools import product

def judge(pro):
    union_set=set()
    for i in range(M):
        if pro[i]:
            union_set|=set(l[i])
    if union_set == W:
        return 1
    else:
        return 0

N,M=map(int,input().split())
l=[[] for _ in range(M)]
W=set(range(1,N+1))
for i in range(M):
    C=int(input())
    l[i]=list(map(int,input().split()))

ans=0
for pro in product((0,1), repeat=M):
    ans+=judge(pro)
print(ans)