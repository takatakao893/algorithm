import sys
sys.setrecursionlimit(10**6)

n=int(input())
Parent=[-1 for _ in range(n)]
Sibling=[-1 for _ in range(n)]
Leaf=[[] for _ in range(n)]
Degree=[0 for _ in range(n)]
Depth=[0 for _ in range(n)]
Height=[0 for _ in range(n)]

for _ in range(n):
    num_id, left, right=map(int,input().split())
    degree=0
    if left!=-1 and right!=-1:
        Sibling[left]=right
        Sibling[right]=left
    if left!=-1:
        Parent[left]=num_id
        Leaf[num_id].append(left)
        degree+=1
    if right!=-1:
        Parent[right]=num_id
        Leaf[num_id].append(right)
        degree+=1
    Degree[num_id]=degree

def dfs(curr,depth):
    Depth[curr]=depth
    height=0
    for child in Leaf[curr]:
        dfs(child,depth+1)
        height = max(height, Height[child]+1)
    Height[curr] = height

root=None
for i in range(n):
    if Parent[i]==-1:
        root=i
        break

dfs(root,0)

for i in range(n):
    print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, ".format(i,Parent[i],Sibling[i],Degree[i],Depth[i],Height[i]),end="")
    if Parent[i]==-1:
        print("root")
    else:
        if len(Leaf[i])==0:
            print("leaf")
        else:
            print("internal node")