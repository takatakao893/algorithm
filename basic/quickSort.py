from copy import deepcopy

def partition(A, p, r):
    x = int(A[r][1])
    i = p-1
    for j in range(p,r):
        if int(A[j][1]) <= x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def quicksort(A,p,r):
    if p<r:
        q=partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)
        
n=int(input())
card=[]
for _ in range(n):
    a,b=input().split()
    card.append([a,int(b)])
    
A=deepcopy(card)
B=deepcopy(card)
B.sort(key=lambda x:x[1])
quicksort(A,0,n-1)
if B==A:
    print("Stable")
else:
    print("Not stable")

for x in A:
    print(*x)
