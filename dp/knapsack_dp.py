# 個数制限なし
n_max=1000
w_max=10000
dp=[[0]*(w_max+1) for _ in range(n_max+1)]

N,W=map(int,input().split())
w=list(map(int,input().split()))
v=list(map(int,input().split()))

# iは商品番号 jは重さ
for i in range(N):
    for j in range(1,W+1):
        if j<w[i]:
            dp[i+1][j]=dp[i][j]
        else:
            dp[i+1][j]=max(dp[i][j],dp[i+1][j-w[i]]+v[i])
print(dp[N][W])

