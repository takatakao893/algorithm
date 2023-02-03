m,n,p=map(int,input().split())
A=[[1]*n for _ in range(m)]
B=[[1]*m for _ in range(n)]
C=[[0]*m for _ in range(m)]

u=0
while u < m:
    v=0
    while v < m:
        w=0
        while w < n:
            i=u
            while i < u+p:
                j=v
                while j < v+p:
                    d=0
                    k=w
                    while k < w+p:
                        d+=A[i][k]*B[k][j]
                        k+=1
                    C[i][j]+=d
                    j+=1
                i+=1
            w+=p
        v+=p
    u+=p
print(C)
                        
                
