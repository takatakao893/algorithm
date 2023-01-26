N,X=map(int,input().split())
cnt=0
# i+j+k=N より k=N-(i+j)
for i in range(1,N+1):
    for j in range(i+1,N+1):
        k = X - i - j
        if j<k and k<=N:
            cnt+=1
print(cnt)
