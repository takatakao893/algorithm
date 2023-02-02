def judge(T):
    daylength=0
    for i in range(N):
        if A[i]>T:
            daylength+=1
        else:
            daylength=0
        if daylength>=P:
            return False
    return True

N,P=map(int,input().split())
A=list(map(int,input().split()))
for t in range(41):
    if judge(t) == True:
        print(t)
        break
        
            
    