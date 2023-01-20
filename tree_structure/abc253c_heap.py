import heapq
from collections import defaultdict
q=int(input())
mn=[]
mx=[]
cnt=defaultdict(int)
# ヒープ木 最小の要素を取り出す
for _ in range(q):
    query=list(map(int,input().split()))
    if query[0]==1:
        x=query[1]
        cnt[x]+=1
        heapq.heappush(mn,x)
        heapq.heappush(mx,-x)
    elif query[0]==2:
        x,c=query[1],query[2]
        cnt[x]=max(0,cnt[x]-c)
    elif query[0]==3:
        while cnt[mn[0]]==0:
            heapq.heappop(mn)
        while cnt[-mx[0]]==0:
            heapq.heappop(mx)
        print(-mx[0]-mn[0])