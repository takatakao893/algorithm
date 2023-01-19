class Node:
    def __init__(self,node_id,node_left,node_right,node_parent):
        self.id=node_id
        self.left=node_left
        self.right=node_right
        self.parent=node_parent

n=int(input())
# インスタンス生成
nodes=[Node(-1,-1,-1,-1) for _ in range(n)]
for _ in range(n):
    id,left,right=map(int,input().split())
    nodes[id].id=id
    nodes[id].left=left
    nodes[id].right=right
    if left!=-1:
        nodes[left].parent=id
    if right!=-1:
        nodes[right].parent=id

root=None
for i in range(n):
    if nodes[i].parent==-1:
        root=nodes[i].id
        break

def pre_order(node_id):
    if node_id == -1:
        return
    print(f' {node_id}',end="")
    pre_order(nodes[node_id].left)
    pre_order(nodes[node_id].right)

def in_order(node_id):
    if node_id == -1:
        return
    in_order(nodes[node_id].left)
    print(f' {node_id}',end="")
    in_order(nodes[node_id].right)

def post_order(node_id):
    if node_id == -1:
        return
    post_order(nodes[node_id].left)
    post_order(nodes[node_id].right)
    print(f' {node_id}',end="")

print("Preorder")
pre_order(root)
print()
print("Inorder")
in_order(root)
print()
print("Postorder")
post_order(root)
print()
