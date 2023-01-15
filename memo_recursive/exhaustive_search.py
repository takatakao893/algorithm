n_max=100
m_max=10000
dp=[[-1]*m_max for _ in range(n_max)]
def solve(i,m):
    if dp[i][m]>=0:
        return dp[i][m]
    if m==0:
        return True
    elif i>=n:
        return False
    else:
        res = solve(i+1,m) or solve(i+1,m-A[i])
        dp[i][m]=res
        return res


n=int(input())
A=list(map(int,input().split()))
q=int(input())
m=list(map(int,input().split()))

for i in range(q):
    if m[i]>sum(A):
        print("no")
    else:
        print("yes" if solve(0,m[i]) else "no")
