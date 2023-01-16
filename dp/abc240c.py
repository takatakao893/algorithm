def solve():
    n_max=100
    x_max=10000
    N,X=map(int,input().split())
    A,B=[],[]
    for _ in range(N):
        a,b=map(int,input().split())
        A.append(a)
        B.append(b)
    dp=[[False]*(x_max+1) for _ in range(n_max+1)]
    # 0回ジャンプで座標0
    dp[0][0]=True
    
    for i in range(N):
        for x in range(X):
            if dp[i][x]:
                if A[i]+x<=X:
                    dp[i+1][A[i]+x]=True
                if B[i]+x<=X:
                    dp[i+1][B[i]+x]=True
    
    return dp[N][X]

print("Yes" if solve() else "No")


    

