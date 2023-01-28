def lcs(X,Y):
    n=len(X)
    m=len(Y)
    # dp[i][j] Sのi文字目までを使って、Tのj文字目まで作る選び方
    dp=[[None]*(9) for _ in range(n)]
    dp[0][0]=1
    for j in range(1,9):
        dp[0][j]=0
    for i in range(1,n):
        dp[i][0]=1
    
    for i in range(1,n):
        for j in range(1,m):
            if X[i]==Y[j]:
                dp[i][j]=dp[i-1][j]+dp[i-1][j-1]
            else:
                # Sのi文字目に下線を引けない
                dp[i][j]=dp[i-1][j]
        dp[i][j] = dp[i][j]%MOD

    return dp[n-1][8]
    
S=input()
S='?'+S
T='?chokudai'
MOD = 10**9+7
print(lcs(S,T))
