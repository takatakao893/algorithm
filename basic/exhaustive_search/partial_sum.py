# bit全探索 (部分和問題)
from itertools import product

def judge(pro):
    S=0
    for i in range(N):
        if pro[i]:
            S+=A[i]
    if S==W:
        return 1
    else:
        return 0

N,W=map(int,input().split())
A=list(map(int,input().split()))

# 判定関数judge
ans=0
for pro in product((0,1), repeat=N):
    ans+=judge(pro)

print(ans)
