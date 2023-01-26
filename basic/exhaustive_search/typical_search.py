N,K=map(int,input().split())
A=list(map(int,input().split()))
cnt=0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if A[i]+A[j]+A[k]==K:
                cnt+=1
print(cnt)