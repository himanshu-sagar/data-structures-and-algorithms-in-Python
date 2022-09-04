class Node:
    def __init__(self):
        self.root=None
        self.lchild=None
        self.rchild=None
def binaryTree():
    from collections import deque
    q=deque()
    print("Enter Root Value: ")
    x=input()
    tree=Node()
    tree.root=x
    tree.lchild=0
    tree.rchild=0
    n=0
    q.append(tree)
    n=n+1
    while(n!=0):
        p=q.popleft()
        n=n-1
        print("Enter Left Child of  "+str(p.root)+" :")
        x=input()
        if (x!=str(-1)):
            newnode=Node()
            newnode.root=x
            p.lchild=newnode
            q.append(newnode)
            n+=1
            
        print("Enter Right Child of "+str(p.root)+" :")
        y=input()
        if (y!=str(-1)):
            newnode=Node()
            newnode.root=y
            p.rchild=newnode
            q.append(newnode)
            n+=1
    return tree
    tree=binaryTree()
    # If you want to insert a null node, input -1
    # To check the Implementation use a traversal method from other file in this repository
    
    
