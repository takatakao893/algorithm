# 連鎖行列積のスカラー乗算数の最小値をdpで求める
n=int(input())
R,C=[],[]
for _ in range(n):
    r,c=map(int,input().split())
    R.append(r)
    C.append(c)

INF=10**19
dp=[[INF]*(n+1) for _ in range(n+1)]
for i in range(n): dp[i][i]=0

for l in range(1,n):
    for i in range(n-l):
        j=l+i
        for k in range(i,j):
            tmp=dp[i][k]+dp[k+1][j]+R[i]*C[k]*C[j]
            dp[i][j]=min(tmp,dp[i][j])

print(dp[0][n-1])

"""
行列数を5と仮定する
for l in range(1,n)
  for i in range(n-l)
    j=l+i             #jとlの関係を並べる
    l=1  j=1,2,3,4,5  i=0~4
    l=2  j=2,3,4,5     i=0~3
    l=3  j=3,4,5        i=0~2
    l=4  j=4,5           i=0~1 
	l=5  j=5              i=0
"""
 
