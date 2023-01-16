N=int(input())
A=list(map(int,input().split()))
B=[0]*N
B[0]=[0,A[0]]
for i in range(1,N):
    B[i] = [0]+[A[i]+x for x in B[i-1]]
B=[x%360 for x in B[N-1]]
B.sort()
B.append(360)
C=[B[i+1]-B[i] for i in range(len(B)-1)]
print(max(C))
