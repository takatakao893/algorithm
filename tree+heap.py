class Node:
    def __init__(self,key,prior):
        self.key = key
        self.left = None
        self.right = None
        self.prior = prior  

class Binary_search_tree:
    def __init__(self):
        self.root = None
        return
    
    def rightRotate(self,t):
        s = t.left
        t.left = s.right
        s.right = t
        if t.key == self.root.key:
            self.root = s
        return s
    
    def leftRotate(self, t):
        s = t.right
        t.right = s.left
        s.left = t
        if t.key == self.root.key:
            self.root = s
        return s
    
    def insert(self,t,z):
        if self.root == None:
            self.root = z
            return
        
        if t == None:
            return z
        if z.key == t.key:
            return t
        
        if z.key < t.key:
            t.left = self.insert(t.left,z)
            if t.prior < t.left.prior: # tの優先度よりも子の優先度が高いとき
                t = self.rightRotate(t)
        else:
            t.right = self.insert(t.right,z)
            if t.prior < t.right.prior: # tの優先度よりも子の優先度が高いとき
                t = self.leftRotate(t)
        return t
    
    def find(self,k):
        x = self.root
        while x!=None:
            if x.key == k:
                print('yes')
                return
            if x.key > k:
                x = x.left
            else:
                x = x.right
        print('no')
        return
    
    def delete(self,t,k):
        if t == None:
            return t
        if k < t.key:
            t.left = self.delete(t.left,k)
        elif k > t.key:
            t.right = self.delete(t.right,k)
        else:
            return self._delete(t,k)
        return t
    
    def _delete(self,t,k):
        if t.left == None and t.right == None:
            return None
        elif t.left == None: # 左の子が存在しない
            t = self.leftRotate(t) # 左に回転
        elif t.right == None: # 右の子が存在しない
            t = self.rightRotate(t) # 右に回転
        else:
            if t.left.prior > t.right.prior: # 左の子の優先度が右の子よりも大きい
                t = self.rightRotate(t) # 右に回転
            else: # 右の子の優先度が左の子よりも大きい
                t = self.leftRotate(t) # 左に回転
        return self.delete(t,k)
    
    def dfs(self,node):
        self.preorder.append(node.key)
        if node.left != None:
            self.dfs(node.left)
        self.inorder.append(node.key)
        if node.right != None:
            self.dfs(node.right)
        return
    
    def print_tree(self):
        self.inorder = []
        self.preorder = []
        self.dfs(self.root)
        print('',*self.inorder)
        print('',*self.preorder)
        return   

Bst = Binary_search_tree()
m = int(input())
for i in range(m):
    l = list(input().split())
    if l[0] == 'print':
        Bst.print_tree()
    elif l[0] == 'insert':
        z = Node(int(l[1]),int(l[2]))
        Bst.insert(Bst.root,z)
    elif l[0] == 'delete':
        Bst.delete(Bst.root,int(l[1]))
    elif l[0] == 'find':
        Bst.find(int(l[1]))     
