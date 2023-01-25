cnt=0
def merge(A, left, mid, right):
    INF=10e18
    L=A[left:mid]+[INF]
    R=A[mid:right]+[INF]
    i=0
    j=0
    for k in range(left,right):
        global cnt
        cnt+=1
        if L[i] <= R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1
    return cnt

def mergeSort(A, left, right):
    if left+1 < right:
        mid = (left+right)//2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)

n=int(input())
S=list(map(int,input().split()))
mergeSort(S,0,n)
print(*S)
print(cnt)
    