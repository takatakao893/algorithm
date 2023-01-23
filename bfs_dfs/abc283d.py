from collections import defaultdict,deque
S=list(input())
key=defaultdict(bool)
deckey=defaultdict(set)
cnt=0
for i in range(len(S)):
    if S[i]=='(':
        cnt+=1
    elif S[i]==')':
        for t in deckey[cnt]:
            key[t]=False
        cnt-=1
    else:
        if key[S[i]]==True:
            print("No")
            exit()
        else:
            key[S[i]]=True
            deckey[cnt].add(S[i])
print("Yes")
        