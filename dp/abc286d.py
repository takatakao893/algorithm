N,X=map(int,input().split())
dp=[[False]*(X+1) for _ in range(N+1)]
# A[i]円をB[i]枚用いて、j円支払う
AB=[tuple(map(int,input().split())) for _ in range(N)]
dp[0][0]=True
for i in range(N):
    for j in range(X+1):
        if not dp[i][j]:
            continue
        A,B = AB[i]
        for k in range(B+1):
            if X < j+A*k:
                continue
            dp[i+1][j+A*k]=True

print("Yes" if any(dp[i][X] for i in range(N+1)) else "No")
