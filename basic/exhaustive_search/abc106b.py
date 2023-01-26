N=int(input())
ans=0
def solve(n):
    cnt=0
    for i in range(1,n+1):
        if n%i==0:
            cnt+=1
    if cnt==8 and n%2==1: 
        return True
    return False

for i in range(1,N+1):
    if solve(i)==True:
        ans+=1
print(ans)
        
    
