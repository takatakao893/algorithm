def selectionSort(A, N):
    cnt=0
    for i in range(N):
        minj = i
        for j in range(i,N):
            if A[j] < A[minj]:
                minj = j
        if i != minj:
            cnt+=1
            A[i],A[minj]=A[minj],A[i]
    return cnt

N=int(input())
A=list(map(int,input().split()))
t=selectionSort(A,N)
print(*A)
print(t)