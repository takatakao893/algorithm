def solve():
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    
    a_ok=[False]*(N+1)
    b_ok=[False]*(N+1)
    a_ok[0]=True
    b_ok[0]=True
    
    for i in range(N-1):
        if a_ok[i]:
            b_ok[i+1] |= abs(B[i+1]-A[i])<=K
            a_ok[i+1] |= abs(A[i+1]-A[i])<=K
        if b_ok[i]:
            a_ok[i+1] |= abs(A[i+1]-B[i])<=K
            b_ok[i+1] |= abs(B[i+1]-B[i])<=K
    
    return a_ok[N-1] or b_ok[N-1]

print("Yes" if solve() else "No")


    

