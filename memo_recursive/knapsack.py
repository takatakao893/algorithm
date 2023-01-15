n_max=1000
w_max=10000
dp=[[-1]*(w_max+1) for _ in range(n_max+1)]
# iは商品番号 jは重さ
def rec(i,j):
    if dp[i][j]>=0:
        return dp[i][j]
    if j==0:
        return 0
    if i>=N:
        return 0
    elif w[i]>j:
        res = rec(i+1,j)
    else:
        res = max(rec(i+1,j),rec(i+1,j-w[i])+v[i])
    dp[i][j]=res
    return res

N,W=map(int,input().split())
w=list(map(int,input().split()))
v=list(map(int,input().split()))
print(rec(0,W))

