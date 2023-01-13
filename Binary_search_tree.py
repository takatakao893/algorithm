class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class Binary_search_tree:
    def __init__(self):
        self.root = None
    
    def insert(self,z):
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        
        z.parent = y    # zの親をyに変更
        
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
    
    def find(self,key):
        x = self.root
        while x!=None:
            if x.key > key:
                x = x.left
            elif x.key < key:
                x = x.right
            else:
                print("yes")
                return
        print("no")
        return
    
    def delete(self, k):
        z = self.root
        while z != None and z.key != k: # 現在地がNoneでなく、かつキーがkでない限り繰り返し
            if z.key > k:
                z = z.left
            else:
                z = z.right
        if z == None:   # 現在地がNoneの場合(キーがkである節点が存在しない場合)、何もしない
            return
        if z.left == None and z.right == None:  # zが葉である場合
            x = z.parent # xをzの親とする
            if x == None:
                self.root = None
            elif x.right == z: # xの右の子がzである場合
                x.right = None
            else:   # xの左の子がzである場合
                x.left = None
        elif z.right != None and z.left != None: # zが二つの子を持つ場合
            y = z.right # yをzの右の子とする
            while y.left != None: # yに左の子が存在する限り繰り返す
                y = y.left
            self.delete(y.key) # yを削除する
            z.key = y.key
        else:   # zがちょうど一つの子を持つ場合
            if z.right != None: # 右の子が存在する場合
                y = z.right
            else: # 左の子が存在する場合
                y = z.left
            x = z.parent
            y.parent = x
            if x==None:
                self.root = y
            elif x.right == z:
                x.right = y
            else:
                x.left = y
    
    def dfs(self,node):
        self.preorder.append(node.key)
        if node.left!=None:
            self.dfs(node.left)
        self.inorder.append(node.key)
        if node.right != None:
            self.dfs(node.right)
    
    
    def print_tree(self):
        self.preorder=[]
        self.inorder=[]
        
        self.dfs(self.root)
        
        print('',*self.inorder)
        print('',*self.preorder)

m=int(input())
Bst = Binary_search_tree() # インスタンス生成
for _ in range(m):
    l=list(input().split())
    if l[0]=='insert':
        Bst.insert(Node(int(l[1])))
    elif l[0]=='find':
        Bst.find(int(l[1]))
    elif l[0]=='print':
        Bst.print_tree()
    else:
        Bst.delete(int(l[1]))            
